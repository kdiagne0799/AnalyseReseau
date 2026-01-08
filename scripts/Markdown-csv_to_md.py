import csv
import os
from collections import Counter

# S'assurer que le script travaille dans son propre répertoire
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def interpret_flags(packet_info):
    """Interprète les drapeaux TCP/IP pour un affichage clair."""
    if "Flags [S]" in packet_info: return "Connection Request (SYN)"
    if "Flags [P.]" in packet_info: return "Data Transfer (PUSH-ACK)"
    if "Flags [.]" in packet_info: return "Acknowledgment (ACK)"
    if "Flags [R]" in packet_info: return "Connection Refused (RST)"
    if "ICMP" in packet_info: return "Ping/Network Diagnostic"
    if "telnet" in packet_info or ".23" in packet_info: return "Unencrypted Telnet"
    return "Other protocol"

def generate_final_report(input_csv, output_md):
    try:
        if not os.path.exists(input_csv):
            print(f"Error: {input_csv} not found.")
            return

        with open(input_csv, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=';')
            packets = list(reader)

        if not packets:
            print("Error: The CSV file is empty.")
            return

        # --- ANALYSE DES DONNÉES ---
        # Analyse SSH
        ssh_packets = [p for p in packets if '.ssh' in p['Destination'] or '.22' in p['Destination']]
        ssh_counts = Counter([p['Source'] for p in ssh_packets])
        
        # Analyse des ports
        dest_ports = [p['Destination'].split('.')[-1] for p in packets]
        unique_dest_ports = len(set(dest_ports))

        # Analyse ICMP et Telnet
        icmp_packets = [p for p in packets if "ICMP" in p['Packet_Info']]
        telnet_attempts = [p for p in packets if "telnet" in p['Destination'] or ".23" in p['Destination']]

        # --- GÉNÉRATION DU MARKDOWN FINAL ---
        with open(output_md, 'w', encoding='utf-8') as md:
            # Titre Principal
            md.write("# 🛡️ Global Network Security Report\n\n")
            
            # Section 1 : Menaces SSH (Formaté pour devenir des cartes d'alerte)
            md.write("## 1. Critical Threat: Targeted SSH Attack\n\n")
            if not ssh_counts:
                md.write("- ✅ **No specific SSH threats detected.**\n")
            else:
                for source, count in ssh_counts.items():
                    if count >= 40:
                        md.write(f"- 🔴 **CRITICAL**: Source `{source}` | **{count} packets** | Brute Force confirmed\n")
                    else:
                        md.write(f"- 🟡 **WARNING**: Source `{source}` | **{count} packets** | Potential Reconnaissance\n")

            # Section 2 : Autres Anomalies
            md.write("\n## 2. Other Detected Anomalies\n\n")
            
            if unique_dest_ports > 5:
                md.write(f"- ⚠️ **Port Scanning**: Host probed **{unique_dest_ports}** different ports.\n")
            
            if len(icmp_packets) > 20:
                md.write(f"- ⚠️ **ICMP Flood**: **{len(icmp_packets)}** packets detected (Potential DoS).\n")

            if telnet_attempts:
                md.write(f"- ❌ **Insecure Protocol**: **{len(telnet_attempts)}** Telnet attempts detected (Port 23).\n")

            if unique_dest_ports <= 5 and len(icmp_packets) <= 20 and not telnet_attempts:
                md.write("- ✅ No secondary anomalies detected.\n")

            # Section 3 : Tableau Technique (ÉCHANTILLON DE 70 LIGNES)
            md.write("\n## 3. Traffic Sample (Top 70)\n\n")
            # Les espaces dans les en-têtes et l'utilisation de ` ` garantissent la séparation
            md.write("| Timestamp         | Source IP / Host        | Flag Meaning                | Technical Summary                                      |\n")
            md.write("| :---------------- | :---------------------- | :-------------------------- | :----------------------------------------------------- |\n")
            
            # Extraction des 70 premières lignes
            for p in packets[:70]:
                time_val = p.get('Timestamp', 'N/A').strip()
                source_val = p.get('Source', 'Unknown').replace('"', '').strip()
                info_val = p.get('Packet_Info', 'N/A').strip()
                
                # Formatage sécurisé pour le rendu HTML/Markdown
                # Les backticks ` ` forcent une police monospace et créent un espacement visuel
                md.write(f"| `{time_val}` | `{source_val}` | **{interpret_flags(info_val)}** | {info_val[:65]}... |\n")

        print(f"✅ Success! Report generated with 70 lines at: {output_md}")

    except Exception as e:
        print(f"💥 Error during report generation: {e}")

if __name__ == "__main__":
    # Configuration des chemins relatifs à la structure Symfony
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(BASE_DIR, '..', 'public', 'Network_Analysis.csv')
    output_file = os.path.join(BASE_DIR, '..', 'Network_Report.md')
    
    generate_final_report(input_file, output_file)