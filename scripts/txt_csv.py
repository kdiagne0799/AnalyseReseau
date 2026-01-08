import csv
import os
from collections import Counter

# S'assurer que le script travaille dans son propre répertoire
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def interpret_flags(packet_info):
    if "Flags [S]" in packet_info: return "Connection Request (SYN)"
    if "Flags [P.]" in packet_info: return "Data Transfer (PUSH-ACK)"
    if "Flags [.]" in packet_info: return "Acknowledgment (ACK)"
    if "Flags [R]" in packet_info: return "Connection Refused (RST)"
    if "ICMP" in packet_info: return "Ping/Network Diagnostic"
    if "telnet" in packet_info or ".23" in packet_info: return "Unencrypted Telnet"
    return "Other protocol"

def generate_final_report(input_csv, output_md):
    try:
        if not os.path.exists(input_csv): return

        with open(input_csv, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=';')
            packets = list(reader)

        if not packets: return

        # Analyse
        ssh_packets = [p for p in packets if '.ssh' in p['Destination'] or '.22' in p['Destination']]
        ssh_counts = Counter([p['Source'] for p in ssh_packets])
        dest_ports = [p['Destination'].split('.')[-1] for p in packets]
        unique_dest_ports = len(set(dest_ports))
        icmp_packets = [p for p in packets if "ICMP" in p['Packet_Info']]
        telnet_attempts = [p for p in packets if "telnet" in p['Destination'] or ".23" in p['Destination']]

        # Génération du Markdown
        with open(output_md, 'w', encoding='utf-8') as md:
            md.write("# 🛡️ Global Network Security Report\n\n")
            
            md.write("## 1. Critical Threat: Targeted SSH Attack\n\n")
            if not ssh_counts:
                md.write("- ✅ **No specific SSH threats detected.**\n")
            else:
                for source, count in ssh_counts.items():
                    status = "🔴 **CRITICAL**" if count >= 40 else "🟡 **WARNING**"
                    md.write(f"- {status}: Source `{source}` | **{count} packets**\n")

            md.write("\n## 2. Other Detected Anomalies\n\n")
            if unique_dest_ports > 5: md.write(f"- ⚠️ **Port Scanning**: Probed **{unique_dest_ports}** ports.\n")
            if len(icmp_packets) > 20: md.write(f"- ⚠️ **ICMP Flood**: **{len(icmp_packets)}** packets.\n")
            if telnet_attempts: md.write(f"- ❌ **Insecure Protocol**: Telnet (Port 23) detected.\n")

            md.write("\n## 3. Traffic Sample \n\n")
            # En-têtes espacés pour forcer la structure
            md.write("| ARRIVAL TIMESTAMP | SOURCE ADDRESS / HOST | FLAG MEANING | TECHNICAL SUMMARY |\n")
            md.write("| :--- | :--- | :--- | :--- |\n")
            
            for p in packets[:70]:
                time_val = p.get('Timestamp', 'N/A')
                source_val = p.get('Source', 'Unknown').replace('"', '')
                info_val = p.get('Packet_Info', 'N/A')
                md.write(f"| `{time_val}` | `{source_val}` | {interpret_flags(info_val)} | {info_val[:50]}... |\n")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    generate_final_report(os.path.join(BASE_DIR, '..', 'public', 'Network_Analysis.csv'), os.path.join(BASE_DIR, '..', 'Network_Report.md'))