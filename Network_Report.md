# 🛡️ Global Network Security Report

## 1. Critical Threat: Targeted SSH Attack

- 🟡 **WARNING**: Source `192.168.190.130.50019` | **4 packets**
- 🔴 **CRITICAL**: Source `192.168.190.130.50245` | **60 packets**
- 🟡 **WARNING**: Source `BP-Linux8.43717` | **6 packets**
- 🟡 **WARNING**: Source `BP-Linux8.34621` | **6 packets**
- 🟡 **WARNING**: Source `192.168.190.130.50374` | **2 packets**

## 2. Other Detected Anomalies

- ⚠️ **Port Scanning**: Probed **135** ports.
- ⚠️ **ICMP Flood**: **84** packets.

## 3. Traffic Sample 

| ARRIVAL TIMESTAMP | SOURCE ADDRESS / HOST | FLAG MEANING | TECHNICAL SUMMARY |
| :--- | :--- | :--- | :--- |
| `15:34:04.766656` | `BP-Linux8.ssh` | Data Transfer (PUSH-ACK) | Flags [P.], seq 2243505564:2243505672, ack 1972915... |
| `15:34:04.766694` | `BP-Linux8.ssh` | Data Transfer (PUSH-ACK) | Flags [P.], seq 108:144, ack 1, win 312, options [... |
| `15:34:04.766723` | `BP-Linux8.ssh` | Data Transfer (PUSH-ACK) | Flags [P.], seq 144:252, ack 1, win 312, options [... |
| `15:34:04.766744` | `BP-Linux8.ssh` | Data Transfer (PUSH-ACK) | Flags [P.], seq 252:288, ack 1, win 312, options [... |
| `15:34:04.785366` | `192.168.190.130.50019` | Acknowledgment (ACK) | Flags [.], ack 108, win 7319, options [nop,nop,TS ... |
| `15:34:04.785384` | `192.168.190.130.50019` | Acknowledgment (ACK) | Flags [.], ack 144, win 7318, options [nop,nop,TS ... |
| `15:34:04.785406` | `192.168.190.130.50019` | Acknowledgment (ACK) | Flags [.], ack 252, win 7316, options [nop,nop,TS ... |
| `15:34:04.785454` | `192.168.190.130.50019` | Acknowledgment (ACK) | Flags [.], ack 288, win 7320, options [nop,nop,TS ... |
| `15:34:05.768334` | `BP-Linux8.58466` | Other protocol | 16550+ PTR? 130.190.168.192.in-addr.arpa. (46)... |
| `15:34:05.769075` | `ns1.lan.rt.domain` | Other protocol | 16550 NXDomain 0/1/0 (112)... |
| `15:34:06.669393` | `192.168.190.130.50245` | Data Transfer (PUSH-ACK) | Flags [P.], seq 1601828178:1601828214, ack 1851233... |
| `15:34:06.669906` | `BP-Linux8.ssh` | Data Transfer (PUSH-ACK) | Flags [P.], seq 1:37, ack 36, win 291, options [no... |
| `15:34:06.679262` | `BP-Linux8.53220` | Other protocol | 54801+ A? lacampora.org. (31)... |
| `15:34:06.679971` | `ns1.lan.rt.domain` | Other protocol | 54801 1/0/0 A 184.107.43.74 (47)... |
| `15:34:06.681188` | `BP-Linux8.ssh` | Data Transfer (PUSH-ACK) | Flags [P.], seq 37:153, ack 36, win 291, options [... |
| `15:34:06.681222` | `BP-Linux8.ssh` | Data Transfer (PUSH-ACK) | Flags [P.], seq 153:189, ack 36, win 291, options ... |
| `15:34:06.681248` | `190-0-175-100.gba.solunet.com.ar.2465` | Connection Request (SYN) | Flags [S], seq 326991629:326991749, win 512, lengt... |
| `15:34:06.681274` | `190-0-175-100.gba.solunet.com.ar.2466` | Connection Request (SYN) | Flags [S], seq 920517760:920517880, win 512, lengt... |
| `15:34:06.681294` | `190-0-175-100.gba.solunet.com.ar.2467` | Connection Request (SYN) | Flags [S], seq 556803824:556803944, win 512, lengt... |
| `15:34:06.681312` | `190-0-175-100.gba.solunet.com.ar.2468` | Connection Request (SYN) | Flags [S], seq 1921632185:1921632305, win 512, len... |
| `15:34:06.681328` | `190-0-175-100.gba.solunet.com.ar.2469` | Connection Request (SYN) | Flags [S], seq 1170972654:1170972774, win 512, len... |
| `15:34:06.681345` | `190-0-175-100.gba.solunet.com.ar.2470` | Connection Request (SYN) | Flags [S], seq 754504426:754504546, win 512, lengt... |
| `15:34:06.681362` | `190-0-175-100.gba.solunet.com.ar.2471` | Connection Request (SYN) | Flags [S], seq 669863147:669863267, win 512, lengt... |
| `15:34:06.681379` | `190-0-175-100.gba.solunet.com.ar.2472` | Connection Request (SYN) | Flags [S], seq 1036593434:1036593554, win 512, len... |
| `15:34:06.681396` | `190-0-175-100.gba.solunet.com.ar.2473` | Connection Request (SYN) | Flags [S], seq 473640609:473640729, win 512, lengt... |
| `15:34:06.681413` | `190-0-175-100.gba.solunet.com.ar.2474` | Connection Request (SYN) | Flags [S], seq 294639309:294639429, win 512, lengt... |
| `15:34:06.681430` | `190-0-175-100.gba.solunet.com.ar.2475` | Connection Request (SYN) | Flags [S], seq 2003734750:2003734870, win 512, len... |
| `15:34:06.681446` | `190-0-175-100.gba.solunet.com.ar.2476` | Connection Request (SYN) | Flags [S], seq 943277646:943277766, win 512, lengt... |
| `15:34:06.681463` | `190-0-175-100.gba.solunet.com.ar.2477` | Connection Request (SYN) | Flags [S], seq 612921749:612921869, win 512, lengt... |
| `15:34:06.681480` | `190-0-175-100.gba.solunet.com.ar.2478` | Connection Request (SYN) | Flags [S], seq 1079269685:1079269805, win 512, len... |
| `15:34:06.681497` | `190-0-175-100.gba.solunet.com.ar.2479` | Connection Request (SYN) | Flags [S], seq 1427118982:1427119102, win 512, len... |
| `15:34:06.681514` | `190-0-175-100.gba.solunet.com.ar.2480` | Connection Request (SYN) | Flags [S], seq 1481846896:1481847016, win 512, len... |
| `15:34:06.681531` | `190-0-175-100.gba.solunet.com.ar.2481` | Connection Request (SYN) | Flags [S], seq 807245684:807245804, win 512, lengt... |
| `15:34:06.681548` | `190-0-175-100.gba.solunet.com.ar.2482` | Connection Request (SYN) | Flags [S], seq 29032482:29032602, win 512, length ... |
| `15:34:06.681564` | `190-0-175-100.gba.solunet.com.ar.2483` | Connection Request (SYN) | Flags [S], seq 2121432424:2121432544, win 512, len... |
| `15:34:06.681581` | `190-0-175-100.gba.solunet.com.ar.2484` | Connection Request (SYN) | Flags [S], seq 266983944:266984064, win 512, lengt... |
| `15:34:06.681597` | `190-0-175-100.gba.solunet.com.ar.2485` | Connection Request (SYN) | Flags [S], seq 780253659:780253779, win 512, lengt... |
| `15:34:06.681614` | `190-0-175-100.gba.solunet.com.ar.2486` | Connection Request (SYN) | Flags [S], seq 426927737:426927857, win 512, lengt... |
| `15:34:06.681630` | `190-0-175-100.gba.solunet.com.ar.2487` | Connection Request (SYN) | Flags [S], seq 2059846495:2059846615, win 512, len... |
| `15:34:06.681647` | `190-0-175-100.gba.solunet.com.ar.2488` | Connection Request (SYN) | Flags [S], seq 485695892:485696012, win 512, lengt... |
| `15:34:06.681664` | `190-0-175-100.gba.solunet.com.ar.2489` | Connection Request (SYN) | Flags [S], seq 1506899314:1506899434, win 512, len... |
| `15:34:06.681681` | `190-0-175-100.gba.solunet.com.ar.2490` | Connection Request (SYN) | Flags [S], seq 1974670292:1974670412, win 512, len... |
| `15:34:06.681697` | `190-0-175-100.gba.solunet.com.ar.2491` | Connection Request (SYN) | Flags [S], seq 984948282:984948402, win 512, lengt... |
| `15:34:06.681722` | `190-0-175-100.gba.solunet.com.ar.2492` | Connection Request (SYN) | Flags [S], seq 2071134208:2071134328, win 512, len... |
| `15:34:06.681739` | `190-0-175-100.gba.solunet.com.ar.2493` | Connection Request (SYN) | Flags [S], seq 582048290:582048410, win 512, lengt... |
| `15:34:06.681756` | `190-0-175-100.gba.solunet.com.ar.2494` | Connection Request (SYN) | Flags [S], seq 1414722580:1414722700, win 512, len... |
| `15:34:06.681773` | `190-0-175-100.gba.solunet.com.ar.2495` | Connection Request (SYN) | Flags [S], seq 1376167161:1376167281, win 512, len... |
| `15:34:06.681789` | `190-0-175-100.gba.solunet.com.ar.2496` | Connection Request (SYN) | Flags [S], seq 793373662:793373782, win 512, lengt... |
| `15:34:06.681806` | `190-0-175-100.gba.solunet.com.ar.2497` | Connection Request (SYN) | Flags [S], seq 586859843:586859963, win 512, lengt... |
| `15:34:06.681823` | `190-0-175-100.gba.solunet.com.ar.2498` | Connection Request (SYN) | Flags [S], seq 1313429529:1313429649, win 512, len... |
| `15:34:06.681839` | `190-0-175-100.gba.solunet.com.ar.2499` | Connection Request (SYN) | Flags [S], seq 599747608:599747728, win 512, lengt... |
| `15:34:06.681856` | `190-0-175-100.gba.solunet.com.ar.2500` | Connection Request (SYN) | Flags [S], seq 1764270382:1764270502, win 512, len... |
| `15:34:06.681872` | `190-0-175-100.gba.solunet.com.ar.2501` | Connection Request (SYN) | Flags [S], seq 1266534982:1266535102, win 512, len... |
| `15:34:06.681889` | `190-0-175-100.gba.solunet.com.ar.2502` | Connection Request (SYN) | Flags [S], seq 1923888203:1923888323, win 512, len... |
| `15:34:06.681906` | `190-0-175-100.gba.solunet.com.ar.2503` | Connection Request (SYN) | Flags [S], seq 477956184:477956304, win 512, lengt... |
| `15:34:06.681924` | `190-0-175-100.gba.solunet.com.ar.2504` | Connection Request (SYN) | Flags [S], seq 1697346829:1697346949, win 512, len... |
| `15:34:06.681941` | `190-0-175-100.gba.solunet.com.ar.2505` | Connection Request (SYN) | Flags [S], seq 1581732153:1581732273, win 512, len... |
| `15:34:06.681958` | `190-0-175-100.gba.solunet.com.ar.2506` | Connection Request (SYN) | Flags [S], seq 2134846905:2134847025, win 512, len... |
| `15:34:06.681975` | `190-0-175-100.gba.solunet.com.ar.2507` | Connection Request (SYN) | Flags [S], seq 5001436:5001556, win 512, length 12... |
| `15:34:06.681992` | `190-0-175-100.gba.solunet.com.ar.2508` | Connection Request (SYN) | Flags [S], seq 100084791:100084911, win 512, lengt... |
| `15:34:06.682008` | `190-0-175-100.gba.solunet.com.ar.2509` | Connection Request (SYN) | Flags [S], seq 1351883007:1351883127, win 512, len... |
| `15:34:06.682025` | `190-0-175-100.gba.solunet.com.ar.2510` | Connection Request (SYN) | Flags [S], seq 892547770:892547890, win 512, lengt... |
| `15:34:06.682041` | `190-0-175-100.gba.solunet.com.ar.2511` | Connection Request (SYN) | Flags [S], seq 203925976:203926096, win 512, lengt... |
| `15:34:06.682058` | `190-0-175-100.gba.solunet.com.ar.2512` | Connection Request (SYN) | Flags [S], seq 93263311:93263431, win 512, length ... |
| `15:34:06.682075` | `190-0-175-100.gba.solunet.com.ar.2513` | Connection Request (SYN) | Flags [S], seq 589592255:589592375, win 512, lengt... |
| `15:34:06.682092` | `190-0-175-100.gba.solunet.com.ar.2514` | Connection Request (SYN) | Flags [S], seq 1666861586:1666861706, win 512, len... |
| `15:34:06.682108` | `190-0-175-100.gba.solunet.com.ar.2515` | Connection Request (SYN) | Flags [S], seq 1444571600:1444571720, win 512, len... |
| `15:34:06.682125` | `190-0-175-100.gba.solunet.com.ar.2516` | Connection Request (SYN) | Flags [S], seq 702975955:702976075, win 512, lengt... |
| `15:34:06.682152` | `190-0-175-100.gba.solunet.com.ar.2517` | Connection Request (SYN) | Flags [S], seq 2016486038:2016486158, win 512, len... |
| `15:34:06.682172` | `190-0-175-100.gba.solunet.com.ar.2518` | Connection Request (SYN) | Flags [S], seq 1002497398:1002497518, win 512, len... |
