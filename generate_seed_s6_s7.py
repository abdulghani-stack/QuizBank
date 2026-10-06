"""
Module by module MCQ generator for:
- Subject 6: Computer Network (2015116)
- Subject 7: Indian Knowledge System (2015511)
"""

def generate_s6_questions(start_id):
    # Subject 6: Computer Network (2015116)
    s_name = "Computer Network"
    s_code = "2015116"
    q_id = start_id
    questions = []

    # S6 M1: Introduction to Computer Networks
    m1_name = "Module I - Introduction to Computer Networks"
    s6_m1 = [
        {
            "topic": "OSI model",
            "question": "Which layer of the 7-layer ISO/OSI Reference Model is responsible for end-to-end process-to-process communication, segmentation, flow control, and port addressing?",
            "option_a": "Transport Layer (Layer 4)",
            "option_b": "Network Layer (Layer 3)",
            "option_c": "Data Link Layer (Layer 2)",
            "option_d": "Session Layer (Layer 5)",
            "answer": "A",
            "explanation": "The Transport Layer (Layer 4) provides logical process-to-process communication, segmenting data, managing port addresses, error recovery, and end-to-end flow control.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Router",
            "question": "At which layer of the OSI model does a standard IP Router operate to forward packets across distinct subnets?",
            "option_a": "Network Layer (Layer 3)",
            "option_b": "Data Link Layer (Layer 2)",
            "option_c": "Physical Layer (Layer 1)",
            "option_d": "Application Layer (Layer 7)",
            "answer": "A",
            "explanation": "Routers operate at the Network Layer (Layer 3), inspecting destination IP addresses and consulting routing tables to forward packets across different networks.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "TCP/IP model",
            "question": "How do the 7 layers of the OSI model map onto the 4 layers of the original DARPA TCP/IP model?",
            "option_a": "Application/Presentation/Session -> Application Layer; Transport -> Transport Layer; Network -> Internet Layer; Data Link/Physical -> Network Access Layer",
            "option_b": "Each OSI layer maps to exactly 2 TCP/IP layers",
            "option_c": "TCP/IP has no transport layer",
            "option_d": "OSI Physical and Data Link become the TCP/IP Internet Layer",
            "answer": "A",
            "explanation": "TCP/IP 4-layer model consolidates Application, Presentation, and Session into the Application Layer, retains Transport, renames Network to Internet, and groups Data Link + Physical into Network Access/Host-to-Network.",
            "difficulty": "medium",
            "question_type": "comparison"
        },
        {
            "topic": "Network topologies",
            "question": "In a Star network topology connected via a central Gigabit Ethernet switch, what occurs if one peripheral workstation's network cable is severed?",
            "option_a": "Only that specific workstation loses network connectivity; all other nodes continue communicating normally through the central switch",
            "option_b": "The entire network crashes and all workstations lose connectivity immediately",
            "option_c": "The central switch catches fire",
            "option_d": "Data packets begin circulating in an infinite ring loop",
            "answer": "A",
            "explanation": "Star topology provides high fault tolerance: each node has a dedicated point-to-point link to the central hub/switch, so single cable failures do not disable the network.",
            "difficulty": "easy",
            "question_type": "scenario"
        },
        {
            "topic": "Transmission media",
            "question": "Why is Single-Mode Optical Fiber preferred over Multi-Mode Optical Fiber for long-distance telecommunication backbones spanning dozens of kilometers?",
            "option_a": "Single-mode fiber has a much narrower core (approx 9 micrometers) allowing light to travel along a single path, virtually eliminating modal dispersion",
            "option_b": "Single-mode fiber is made of copper wire instead of glass",
            "option_c": "Multi-mode fiber can only transmit sound waves",
            "option_d": "Single-mode fiber requires zero optical transceivers",
            "answer": "A",
            "explanation": "Single-mode fiber's tiny core permits only one ray/mode of light propagation, eliminating modal dispersion and enabling high bandwidth over 100+ km without repeaters.",
            "difficulty": "medium",
            "question_type": "comparison"
        },
        {
            "topic": "Switch",
            "question": "How does a Layer 2 Ethernet Switch populate its MAC Address Table (Content Addressable Memory / CAM table)?",
            "option_a": "By inspecting the Source MAC address of incoming frames and recording the associated ingress physical switch port",
            "option_b": "By querying a centralized DNS server on the internet",
            "option_c": "By randomly assigning MAC addresses to switch ports",
            "option_d": "By inspecting destination TCP port numbers",
            "answer": "A",
            "explanation": "Switches learn dynamically via backward learning: reading the frame's Source MAC address and noting which physical port it arrived on, updating the CAM forwarding table.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "LAN",
            "question": "What is the typical geographic span that characterizes a Local Area Network (LAN) compared to a Wide Area Network (WAN)?",
            "option_a": "A single room, building, or university campus (typically within a few kilometers), characterized by high data transfer rates and low propagation delay",
            "option_b": "An entire continent or global satellite link",
            "option_c": "A personal body area network spanning 10 centimeters",
            "option_d": "An interplanetary deep space communications link",
            "answer": "A",
            "explanation": "LANs cover small geographic areas (homes, offices, campus buildings) privately owned by one organization with high bandwidth (1 Gbps - 100 Gbps) and low latency.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Gateway",
            "question": "What is the primary function of an Application Gateway / Protocol Converter in heterogeneous networking?",
            "option_a": "It translates communication protocols and data formats between completely disparate network architectures operating across all 7 layers of the OSI stack",
            "option_b": "It only amplifies electrical signals at the Physical Layer",
            "option_c": "It splits fiber optic cables into copper lines",
            "option_d": "It replaces Ethernet cabling with coaxial lines",
            "answer": "A",
            "explanation": "Gateways operate at higher layers (up to Application Layer), performing complex protocol translation (e.g. bridging legacy SNA networks with modern IP networks or email format conversion).",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Peer-to-peer",
            "question": "How does a Peer-to-Peer (P2P) network architecture differ fundamentally from a Client-Server architecture?",
            "option_a": "In P2P, every participating node (peer) acts as both a client and a server with equal privileges, sharing resources directly without a centralized server",
            "option_b": "In P2P, only 1 master node is allowed to transmit data",
            "option_c": "Client-server networks do not require any IP addresses",
            "option_d": "P2P networks cannot transfer files over the internet",
            "answer": "A",
            "explanation": "In Client-Server, centralized servers fulfill requests from passive clients. In P2P (e.g. BitTorrent), each node simultaneously consumes and provides bandwidth and storage.",
            "difficulty": "easy",
            "question_type": "comparison"
        },
        {
            "topic": "Bridge",
            "question": "What is the primary benefit of deploying a Transparent Bridge to segment a large shared Ethernet collision domain into two segments?",
            "option_a": "It divides the single collision domain into two separate collision domains, reducing packet collisions while maintaining a single unified broadcast domain",
            "option_b": "It converts all IPv4 packets into IPv6 packets",
            "option_c": "It eliminates the need for MAC addresses on network interface cards",
            "option_d": "It routes packets across public internet backbones",
            "answer": "A",
            "explanation": "Bridges operate at Layer 2: forwarding frames based on MAC addresses, isolating collisions within local segments while forwarding broadcasts across both segments.",
            "difficulty": "medium",
            "question_type": "conceptual"
        }
    ]
    for q in s6_m1:
        q.update({"id": q_id, "subject": s_name, "subject_code": s_code, "module": m1_name, "module_number": 1})
        questions.append(q)
        q_id += 1

    # S6 M2: Data Link Layer
    m2_name = "Module II - Data Link Layer"
    s6_m2 = [
        {
            "topic": "CRC",
            "question": "Given a data bit sequence D = 1010000 and generator polynomial G(x) = x^3 + 1 (binary divisor 1001), what is the 3-bit Cyclic Redundancy Check (CRC) remainder computed via modulo-2 binary division?",
            "option_a": "011",
            "option_b": "101",
            "option_c": "000",
            "option_d": "111",
            "answer": "A",
            "explanation": "Append 3 zeros to D: 1010000000. Modulo-2 division by 1001: 1010000000 / 1001 yields remainder 011. Transmitted codeword is 1010000011.",
            "difficulty": "medium",
            "question_type": "numerical"
        },
        {
            "topic": "Hamming Codes",
            "question": "In a (7, 4) Hamming Code with 4 data bits (d1, d2, d3, d4) and 3 parity bits (p1, p2, p3), what is the minimum Hamming distance d_min between valid codewords, and what error correction capability does it provide?",
            "option_a": "d_min = 3; capable of detecting up to 2-bit errors and correcting any single 1-bit error",
            "option_b": "d_min = 1; capable of no error detection",
            "option_c": "d_min = 5; capable of correcting 3-bit burst errors",
            "option_d": "d_min = 2; capable of correcting 2-bit errors",
            "answer": "A",
            "explanation": "Richard Hamming proved: to detect e errors requires d_min >= e + 1; to correct t errors requires d_min >= 2t + 1. For d_min = 3: corrects 1 error ((3-1)/2 = 1) and detects 2.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "CSMA/CD",
            "question": "In CSMA/CD (Carrier Sense Multiple Access with Collision Detection) used in classic half-duplex Ethernet (IEEE 802.3), why must the minimum frame transmission time be at least 2 * T_prop (twice the maximum propagation delay)?",
            "option_a": "To ensure a transmitting node is still actively transmitting when a collision signal from the farthest possible network node travels back, allowing collision detection",
            "option_b": "To allow the cable to cool down between transmissions",
            "option_c": "To ensure the frame contains exactly 10,000 bytes",
            "option_d": "Because light travels at infinite speed in copper",
            "answer": "A",
            "explanation": "If a frame is too short, transmission finishes before the collision signal returns (round-trip propagation 2*T_prop), causing the sender to falsely believe transmission succeeded without retransmitting.",
            "difficulty": "hard",
            "question_type": "conceptual"
        },
        {
            "topic": "Slotted ALOHA",
            "question": "What is the maximum theoretical channel utilization (throughput efficiency S) of Slotted ALOHA compared to Pure ALOHA?",
            "option_a": "Slotted ALOHA maximum S = 1/e approx 36.8%; Pure ALOHA maximum S = 1/(2e) approx 18.4%",
            "option_b": "Slotted ALOHA = 100%; Pure ALOHA = 50%",
            "option_c": "Slotted ALOHA = 18.4%; Pure ALOHA = 36.8%",
            "option_d": "Both protocols have identical maximum throughput of 50%",
            "answer": "A",
            "explanation": "Slotted ALOHA restricts transmissions to synchronized slot boundaries, halving vulnerable period from 2T to T. S = G*e^(-G); max S at G=1 is 1/e = 0.368 (36.8%). Pure ALOHA max is 18.4%.",
            "difficulty": "medium",
            "question_type": "numerical"
        },
        {
            "topic": "Sliding Window",
            "question": "In a Go-Back-N sliding window ARQ protocol with an m-bit sequence number, what is the maximum sender window size W_s to prevent protocol failure?",
            "option_a": "W_s <= 2^m - 1",
            "option_b": "W_s <= 2^m",
            "option_c": "W_s <= 2^(m-1)",
            "option_d": "W_s = 2^m + 1",
            "answer": "A",
            "explanation": "In Go-Back-N, sender window must not exceed 2^m - 1. If W_s = 2^m, if all ACKs are lost, retransmitted frames would have sequence numbers ambiguous with new frames.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "CSMA/CA",
            "question": "Why does Wi-Fi (IEEE 802.11) employ CSMA/CA (Collision Avoidance) with RTS/CTS handshake rather than CSMA/CD used in wired Ethernet?",
            "option_a": "Wireless transceivers cannot detect collisions while transmitting due to the Hidden Terminal Problem and because transmitted signal power drowns out received collision signals",
            "option_b": "Wi-Fi radio waves do not travel at the speed of light",
            "option_c": "Wi-Fi access points do not use MAC addresses",
            "option_d": "CSMA/CD is legally prohibited on wireless radio bands",
            "answer": "A",
            "explanation": "In wireless, signal attenuation means transmitted signal is millions of times stronger than incoming echoes. Collision detection is impossible, so RTS/CTS and inter-frame spacing (IFS) avoid collisions.",
            "difficulty": "hard",
            "question_type": "comparison"
        },
        {
            "topic": "Stop and Wait",
            "question": "A satellite link has a one-way propagation delay T_prop = 250 ms and bandwidth B = 1 Mbps. A Stop-and-Wait protocol sends 10,000-bit data frames (transmission time T_trans = 10 ms). What is the line utilization efficiency U?",
            "option_a": "U = T_trans / (T_trans + 2*T_prop) = 10ms / (10ms + 500ms) = 10 / 510 approx 1.96%",
            "option_b": "U = 50%",
            "option_c": "U = 98.04%",
            "option_d": "U = 25.0%",
            "answer": "A",
            "explanation": "Round-trip time RTT = 2 * 250ms = 500ms. Total cycle time = 10ms + 500ms = 510ms. Utilization U = 10 / 510 = 0.0196 (1.96%), illustrating extreme inefficiency of Stop-and-Wait on high delay links.",
            "difficulty": "hard",
            "question_type": "numerical"
        },
        {
            "topic": "Framing",
            "question": "In byte-oriented framing with character stuffing, what escape sequence is inserted if the data payload contains the special byte pattern 'FLAG' or 'ESC'?",
            "option_a": "An 'ESC' (escape) byte is stuffed immediately before any 'FLAG' or 'ESC' byte in the data, and removed by the receiver",
            "option_b": "The frame is deleted and aborted",
            "option_c": "Five consecutive '1' bits are inserted",
            "option_d": "The byte is replaced with a null zero byte",
            "answer": "A",
            "explanation": "Character/Byte Stuffing: whenever the sender encounters a reserved FLAG (0x7E) or ESC (0x7D) byte in payload, it precedes it with an ESC byte. Receiver removes ESC bytes upon reception.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "IEEE 802.3",
            "question": "What is the standard MAC address format and length used in IEEE 802.3 Ethernet network interfaces?",
            "option_a": "48 bits (6 bytes), represented as 12 hexadecimal digits (e.g. 00:1A:2B:3C:4D:5E), with first 24 bits denoting the OUI (Organizationally Unique Identifier)",
            "option_b": "32 bits (4 bytes) in dotted decimal format",
            "option_c": "128 bits represented in colon-separated hex groups",
            "option_d": "64 bits encoded in Base64",
            "answer": "A",
            "explanation": "MAC-48 / EUI-48 addresses are 48 bits long: the first 3 bytes (24 bits) identify the vendor/manufacturer (OUI assigned by IEEE), and the remaining 3 bytes are the unique device serial.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Parity",
            "question": "What is the primary limitation of a Simple 1-bit Even Parity Check code added to an 8-bit data byte?",
            "option_a": "It can detect any single-bit error (or odd number of errors), but completely fails to detect an even number of bit errors (e.g. 2-bit error)",
            "option_b": "It requires 8 additional parity bits per byte",
            "option_c": "It cannot be implemented in hardware logic gates",
            "option_d": "It can correct 4-bit burst errors automatically",
            "answer": "A",
            "explanation": "Simple 1-bit parity counts total 1s. Flipping 2 bits maintains the same parity sum, masking double-bit errors completely from detection.",
            "difficulty": "easy",
            "question_type": "conceptual"
        }
    ]
    for q in s6_m2:
        q.update({"id": q_id, "subject": s_name, "subject_code": s_code, "module": m2_name, "module_number": 2})
        questions.append(q)
        q_id += 1

    # S6 M3: Network Layer
    m3_name = "Module III - Network Layer"
    s6_m3 = [
        {
            "topic": "Subnetting",
            "question": "An IP block `192.168.10.0/26` is allocated to an organization. What are the Subnet Mask, Number of Usable Host IPs, Network Address, and Broadcast Address?",
            "option_a": "Subnet Mask: 255.255.255.192; Usable Hosts: 62; Network: 192.168.10.0; Broadcast: 192.168.10.63",
            "option_b": "Subnet Mask: 255.255.255.128; Usable Hosts: 126; Network: 192.168.10.0; Broadcast: 192.168.10.127",
            "option_c": "Subnet Mask: 255.255.255.224; Usable Hosts: 30; Network: 192.168.10.0; Broadcast: 192.168.10.31",
            "option_d": "Subnet Mask: 255.255.255.0; Usable Hosts: 254; Network: 192.168.10.0; Broadcast: 192.168.10.255",
            "answer": "A",
            "explanation": "/26 leaves 32 - 26 = 6 host bits. 2^6 = 64 total addresses. Usable hosts = 64 - 2 = 62. Mask = 11111111.11111111.11111111.11000000 = 255.255.255.192. Network = .0, Broadcast = .63.",
            "difficulty": "medium",
            "question_type": "numerical"
        },
        {
            "topic": "CIDR",
            "question": "A router receives a packet with destination IP `172.16.15.200`. The routing table has entries:\n1. `172.16.0.0/16` -> Interface 1\n2. `172.16.15.0/24` -> Interface 2\n3. `172.16.15.192/26` -> Interface 3\nUnder the Longest Prefix Match rule, which interface forwards the packet?",
            "option_a": "Interface 3 (matching the most specific /26 prefix: 172.16.15.192 to 172.16.15.255)",
            "option_b": "Interface 1 (matching the /16 prefix)",
            "option_c": "Interface 2 (matching the /24 prefix)",
            "option_d": "The packet is dropped as ambiguous",
            "answer": "A",
            "explanation": "CIDR routing uses Longest Prefix Match. Destination .200 falls within /16, /24, and /26. The /26 prefix (Interface 3) is the longest/most specific mask (26 bits), so it is selected.",
            "difficulty": "medium",
            "question_type": "algorithm_tracing"
        },
        {
            "topic": "NAT",
            "question": "How does Network Address Translation with Port Address Translation (NAT/NAPT) allow hundreds of internal private LAN devices (e.g. 192.168.1.0/24) to access the internet using a single public IPv4 address?",
            "option_a": "By mapping unique internal (Private IP, Source Port) tuples to the single (Public IP, Unique Assigned Port) in a dynamic NAT translation table",
            "option_b": "By encrypting all packets with quantum keys",
            "option_c": "By assigning a permanent public IPv4 address to every lightbulb",
            "option_d": "By converting IP packets into raw physical radio waves",
            "answer": "A",
            "explanation": "NAPT / IP Masquerading multiplexes multiple private IP connections onto a single public IP by translating Layer 4 source port numbers and tracking mappings in its stateful translation table.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "OSPF",
            "question": "What routing algorithm does Open Shortest Path First (OSPF) execute to compute loop-free shortest paths to all destination subnets?",
            "option_a": "Dijkstra's Link-State Algorithm executed on a synchronized Link State Database (LSDB)",
            "option_b": "Bellman-Ford Distance Vector Algorithm",
            "option_c": "Floyd-Warshall all-pairs shortest path",
            "option_d": "A* search algorithm with Euclidean heuristics",
            "answer": "A",
            "explanation": "OSPF is a Link-State protocol (IGP). Routers flood Link-State Advertisements (LSAs) so every router builds an identical topology map (LSDB), then runs Dijkstra's algorithm to compute shortest path trees.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Count-to-Infinity",
            "question": "In Distance Vector routing protocols (such as RIP based on Bellman-Ford), what mechanism prevents two routers from bouncing routing loops indefinitely when a link breaks?",
            "option_a": "Split Horizon, Poison Reverse, and setting infinity to a small maximum metric (e.g. 16 hops in RIP)",
            "option_b": "Increasing the hop count limit to 1,000,000",
            "option_c": "Deleting all routing tables on every clock tick",
            "option_d": "Replacing IP routers with Ethernet hubs",
            "answer": "A",
            "explanation": "Distance Vector protocols resolve Count-to-Infinity via: Split Horizon (never advertise a route back out the interface it was learned from), Poison Reverse (advertise cost=infinity), and max hop limit=16.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "ARP",
            "question": "When Host A wants to send an IP packet to Host B on the same local subnet but only knows Host B's IP address, how does Address Resolution Protocol (ARP) discover Host B's MAC address?",
            "option_a": "Host A broadcasts an ARP Request frame (destination MAC FF:FF:FF:FF:FF:FF) asking 'Who has this IP?'; Host B responds with a unicast ARP Reply containing its MAC address",
            "option_b": "Host A queries the root DNS server over TCP port 53",
            "option_c": "Host A sends an email to the network administrator",
            "option_d": "Host A randomly guesses MAC addresses until one works",
            "answer": "A",
            "explanation": "ARP operates via broadcast request ('Who has IP x.x.x.x? Tell MAC y:y:y:y') and unicast reply from the owner ('I have that IP, my MAC is z:z:z:z'), caching the result in the ARP table.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "ICMP",
            "question": "Which diagnostic network utility uses ICMP Echo Request and Echo Reply messages to test end-to-end host reachability and measure round-trip time?",
            "option_a": "Ping",
            "option_b": "Traceroute (using UDP/TTL expiration)",
            "option_c": "Netstat",
            "option_d": "Nslookup",
            "answer": "A",
            "explanation": "`ping` sends ICMP Type 8 (Echo Request) packets and listens for ICMP Type 0 (Echo Reply) packets from the destination to measure round-trip latency and packet loss.",
            "difficulty": "easy",
            "question_type": "application"
        },
        {
            "topic": "BGP",
            "question": "What makes Border Gateway Protocol (BGP-4) the de facto exterior gateway routing protocol connecting Autonomous Systems (AS) across the global Internet?",
            "option_a": "It is a Path-Vector protocol that exchanges AS-PATH attributes, enabling policy-based inter-domain routing and guaranteeing loop prevention across administrative domains",
            "option_b": "It uses hop-count metrics with a maximum limit of 15 hops",
            "option_c": "It runs exclusively over raw physical fiber without TCP",
            "option_d": "It requires all global internet routers to share a single root password",
            "answer": "A",
            "explanation": "BGP connects autonomous systems (ISPs, cloud providers) using Path-Vector routing over TCP port 179. The `AS_PATH` attribute lists every AS traversed, preventing inter-domain routing loops.",
            "difficulty": "hard",
            "question_type": "conceptual"
        },
        {
            "topic": "IPv6",
            "question": "What is the address space size of IPv6 compared to IPv4, and what mechanism replaces broadcast in IPv6?",
            "option_a": "IPv6 uses 128-bit addresses (approx 3.4 x 10^38 addresses); it eliminates broadcast completely, replacing it with Multicast and Anycast addressing",
            "option_b": "IPv6 uses 64-bit addresses and retains broadcast",
            "option_c": "IPv6 uses 32-bit addresses formatted in hex",
            "option_d": "IPv6 has fewer addresses than IPv4",
            "answer": "A",
            "explanation": "IPv4 has 2^32 (4.3 billion) addresses. IPv6 provides 128-bit (2^128 = 3.4x10^38) addresses, eliminating broadcast in favor of targeted Multicast (e.g. FF02::1 for all nodes) and Anycast.",
            "difficulty": "easy",
            "question_type": "comparison"
        },
        {
            "topic": "Circuit switching",
            "question": "What is the fundamental difference in resource allocation between Circuit Switching (traditional PSTN telephone network) and Packet Switching (the Internet)?",
            "option_a": "Circuit Switching establishes a dedicated end-to-end physical/virtual channel with reserved bandwidth before communication; Packet Switching shares bandwidth dynamically using statistical multiplexing",
            "option_b": "Packet switching reserves 100% of network cables for 1 user",
            "option_c": "Circuit switching breaks data into discrete independent packets",
            "option_d": "Packet switching cannot transmit digital data",
            "answer": "A",
            "explanation": "Circuit switching reserves dedicated capacity (guaranteed bandwidth, no congestion, wasted idle capacity). Packet switching breaks data into packets routed on-demand, maximizing link efficiency.",
            "difficulty": "easy",
            "question_type": "comparison"
        }
    ]
    for q in s6_m3:
        q.update({"id": q_id, "subject": s_name, "subject_code": s_code, "module": m3_name, "module_number": 3})
        questions.append(q)
        q_id += 1

    # S6 M4: Transport Layer
    m4_name = "Module IV - Transport Layer"
    s6_m4 = [
        {
            "topic": "Connection establishment",
            "question": "What is the exact sequence of control flags exchanged during the standard TCP Three-Way Handshake?",
            "option_a": "1. Client -> Server: SYN (seq=x); 2. Server -> Client: SYN-ACK (seq=y, ack=x+1); 3. Client -> Server: ACK (seq=x+1, ack=y+1)",
            "option_b": "1. Client -> Server: ACK; 2. Server -> Client: NAK; 3. Client -> Server: FIN",
            "option_c": "1. Client -> Server: HELLO; 2. Server -> Client: WELCOME",
            "option_d": "1. Client -> Server: DATA; 2. Server -> Client: CONFIRM",
            "answer": "A",
            "explanation": "TCP 3-way handshake synchronizes Initial Sequence Numbers (ISNs) and acknowledges readiness: Client sends SYN, Server replies with SYN+ACK, and Client completes with ACK.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Congestion control",
            "question": "In TCP Tahoe/Reno congestion control, what occurs during the 'Slow Start' phase upon receiving positive acknowledgments?",
            "option_a": "The Congestion Window (cwnd) increases exponentially, doubling every round-trip time (adding 1 MSS to cwnd for every ACK received) until cwnd reaches ssthresh",
            "option_b": "The transmission rate is capped at 1 byte per hour",
            "option_c": "The server immediately disconnects all TCP sockets",
            "option_d": "The window size decreases by 50% on every ACK",
            "answer": "A",
            "explanation": "Despite its name, Slow Start increases transmission rate exponentially: cwnd doubles every RTT (1 -> 2 -> 4 -> 8 MSS) until hitting `ssthresh`, where it switches to linear Congestion Avoidance.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "UDP",
            "question": "Why is UDP (User Datagram Protocol) preferred over TCP for real-time multiplayer gaming, live voice (VoIP), and video streaming?",
            "option_a": "UDP has zero connection setup latency, no head-of-line blocking retransmissions, and minimal 8-byte header overhead, favoring timeliness over 100% reliable delivery",
            "option_b": "UDP guarantees zero packet loss on any network",
            "option_c": "UDP encrypts audio streams using quantum algorithms",
            "option_d": "UDP runs faster because it requires a 10-way handshake",
            "answer": "A",
            "explanation": "TCP's reliable retransmissions cause head-of-line blocking (stalling real-time audio while waiting for old lost packets). UDP drops late packets and delivers freshest audio/game state instantly.",
            "difficulty": "easy",
            "question_type": "comparison"
        },
        {
            "topic": "Flow control",
            "question": "How does TCP's Sliding Window Flow Control prevent a fast transmitting sender from overwhelming a slow receiving host's memory buffer?",
            "option_a": "The receiver advertises its available buffer space in the 'Receive Window' (rwnd) field of every TCP ACK header, and the sender limits unacknowledged in-flight bytes to <= rwnd",
            "option_b": "By shutting down the sender's network interface card",
            "option_c": "By converting TCP packets into UDP datagrams",
            "option_d": "By requiring the sender to pause for 10 seconds between every packet",
            "answer": "A",
            "explanation": "TCP flow control is end-to-end: the receiver informs the sender of remaining buffer capacity via `rwnd`. If `rwnd = 0`, sender halts data transmission until a window update ACK arrives.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Socket programming",
            "question": "In standard BSD Socket Programming in C/Python for a TCP server, which sequence of system calls must be executed before the server can read client data?",
            "option_a": "socket() -> bind() -> listen() -> accept()",
            "option_b": "socket() -> connect() -> send() -> close()",
            "option_c": "open() -> read() -> write() -> delete()",
            "option_d": "listen() -> connect() -> bind() -> start()",
            "answer": "A",
            "explanation": "TCP Server lifecycle: create endpoint (`socket()`), bind to local IP and Port (`bind()`), enter passive listening state (`listen()`), and block waiting for incoming client handshake (`accept()`).",
            "difficulty": "medium",
            "question_type": "code_debugging"
        },
        {
            "topic": "Connection release",
            "question": "In TCP connection termination (Four-Way Handshake), why does the client host enter the `TIME_WAIT` state for 2*MSL (Maximum Segment Lifetime) before closing?",
            "option_a": "To ensure the final ACK reached the server (resending if server retransmits FIN) and to prevent lingering delayed segments from a previous connection from corrupting a new connection",
            "option_b": "To allow the server to download software updates",
            "option_c": "Because TCP connections cannot be closed cleanly",
            "option_d": "To test if the network cable is still plugged in",
            "answer": "A",
            "explanation": "2*MSL (typically 1-2 minutes) in TIME_WAIT ensures any stray duplicate packets die out on the internet, and allows resending the final ACK if it was lost, preventing broken socket resets.",
            "difficulty": "hard",
            "question_type": "conceptual"
        },
        {
            "topic": "TCP timers",
            "question": "In TCP transmission, what formula does Jacobson's algorithm use to dynamically calculate the Retransmission Timeout (RTO) from the smoothed Round Trip Time (SRTT) and RTT Variation (RTTVAR)?",
            "option_a": "RTO = SRTT + 4 * RTTVAR",
            "option_b": "RTO = SRTT / 2",
            "option_c": "RTO = 100 * RTTVAR",
            "option_d": "RTO is always a fixed constant equal to 500 ms",
            "answer": "A",
            "explanation": "RFC 6298 computes dynamic RTO: `SRTT = (1-alpha)*SRTT + alpha*RTT_sample`; `RTTVAR = (1-beta)*RTTVAR + beta*|SRTT - RTT_sample|`; `RTO = SRTT + 4*RTTVAR` (with minimum 1 sec).",
            "difficulty": "hard",
            "question_type": "numerical"
        },
        {
            "topic": "QoS",
            "question": "In Quality of Service (QoS) traffic policing and shaping, how does the 'Token Bucket' algorithm differ from the 'Leaky Bucket' algorithm?",
            "option_a": "Token Bucket permits bursty traffic up to the bucket capacity while maintaining an average rate; Leaky Bucket forces a strictly constant, rigid output transmission rate regardless of burstiness",
            "option_b": "Leaky Bucket allows infinite burst size without packet drops",
            "option_c": "Token Bucket only works on wireless networks",
            "option_d": "Both algorithms drop 100% of all packets during peak hours",
            "answer": "A",
            "explanation": "Leaky bucket enforces a constant outflow rate (smoothing bursts into steady stream). Token bucket accumulates tokens, allowing traffic bursts to pass at wire speed as long as tokens are available.",
            "difficulty": "medium",
            "question_type": "comparison"
        },
        {
            "topic": "Addressing",
            "question": "What is the standard port number assigned by IANA for the following well-known services: HTTP, HTTPS, SSH, and DNS?",
            "option_a": "HTTP: 80, HTTPS: 443, SSH: 22, DNS: 53",
            "option_b": "HTTP: 21, HTTPS: 25, SSH: 8080, DNS: 110",
            "option_c": "HTTP: 443, HTTPS: 80, SSH: 53, DNS: 22",
            "option_d": "HTTP: 8080, HTTPS: 8443, SSH: 23, DNS: 67",
            "answer": "A",
            "explanation": "Well-known system ports: HTTP (80/TCP), HTTPS (443/TCP), SSH (22/TCP), DNS (53/UDP & TCP).",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Multiplexing",
            "question": "How does the Transport Layer achieve Socket Demultiplexing on a multi-application host system?",
            "option_a": "By inspecting the destination Port Number (for UDP) or 4-tuple (Source IP, Source Port, Dest IP, Dest Port for TCP) in incoming headers to deliver data to the correct application socket",
            "option_b": "By broadcasting every incoming packet to all running desktop windows",
            "option_c": "By checking the hard disk file extension",
            "option_d": "By converting TCP packets into email messages",
            "answer": "A",
            "explanation": "Demultiplexing delivers incoming transport segments to the specific socket identified by port numbers (connectionless UDP 2-tuple: dest IP/port; connection-oriented TCP 4-tuple: src/dest IP/port).",
            "difficulty": "easy",
            "question_type": "conceptual"
        }
    ]
    for q in s6_m4:
        q.update({"id": q_id, "subject": s_name, "subject_code": s_code, "module": m4_name, "module_number": 4})
        questions.append(q)
        q_id += 1

    # S6 M5: Application Layer
    m5_name = "Module V - Application Layer"
    s6_m5 = [
        {
            "topic": "DNS",
            "question": "In the Domain Name System (DNS) resolution hierarchy, what type of DNS query occurs when a local DNS resolver queries Root servers (.), TLD servers (.com), and Authoritative servers sequentially on behalf of a client?",
            "option_a": "Iterative Query (non-recursive referral query)",
            "option_b": "Recursive Query from the root to the client",
            "option_c": "Broadcast query across the local subnet",
            "option_d": "Reverse ARP lookup",
            "answer": "A",
            "explanation": "Clients make recursive queries to the local resolver ('give me the answer'). The local resolver makes iterative queries to Root -> TLD -> Authoritative name servers to resolve the domain.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "HTTP",
            "question": "What major performance improvements were introduced in HTTP/2 (RFC 7540) compared to legacy HTTP/1.1?",
            "option_a": "Binary framing, full bidirectional request/response multiplexing over a single TCP connection, HPACK header compression, and Server Push",
            "option_b": "HTTP/2 replaced TCP with raw UDP without encryption",
            "option_c": "HTTP/2 requires opening a separate TCP connection for every image file",
            "option_d": "HTTP/2 eliminated all HTTP status codes",
            "answer": "A",
            "explanation": "HTTP/2 replaced plaintext HTTP/1.1 with binary frames, allowing concurrent multiplexed requests/responses over one TCP connection, eliminating head-of-line blocking and header redundancy.",
            "difficulty": "easy",
            "question_type": "comparison"
        },
        {
            "topic": "Web caching",
            "question": "In HTTP caching mechanisms, what response header directive allows a client to revalidate a cached resource using an ETag (Entity Tag) validator?",
            "option_a": "Client sends `If-None-Match: \"etag-value\"`; if unchanged, server responds with `304 Not Modified` without payload body",
            "option_b": "Client sends `Delete-Cache: true`; server returns `200 OK`",
            "option_c": "Client re-downloads the entire 50MB file on every millisecond",
            "option_d": "Server returns `404 Not Found` to force cache invalidation",
            "answer": "A",
            "explanation": "Conditional GET requests using `If-None-Match: <etag>` allow servers to return `304 Not Modified` with zero body bytes if content hasn't changed, saving immense bandwidth.",
            "difficulty": "medium",
            "question_type": "application"
        },
        {
            "topic": "SMTP",
            "question": "In electronic mail architecture, what are the distinct roles of SMTP versus POP3 / IMAP?",
            "option_a": "SMTP (Simple Mail Transfer Protocol) is a push protocol used to send/relay emails between servers; POP3/IMAP are pull protocols used by email clients to retrieve messages from mailboxes",
            "option_b": "SMTP is used to download emails to phones while IMAP is used to send emails",
            "option_c": "POP3 keeps all emails synchronized across 10 devices in real time",
            "option_d": "SMTP can only send emails containing plain text without attachments",
            "answer": "A",
            "explanation": "SMTP pushes messages from mail client to mail server and between MTA servers (port 25/587). POP3/IMAP are mail access retrieval protocols (pulling mail down to user client MUA).",
            "difficulty": "easy",
            "question_type": "comparison"
        },
        {
            "topic": "DHCP",
            "question": "What is the 4-step DORA message exchange used by Dynamic Host Configuration Protocol (DHCP) to automatically lease an IP address to a newly joined client?",
            "option_a": "1. DHCP Discover (broadcast) -> 2. DHCP Offer (unicast/broadcast) -> 3. DHCP Request (broadcast) -> 4. DHCP Acknowledge (unicast/broadcast)",
            "option_b": "1. Connect -> 2. Authenticate -> 3. Authorize -> 4. Disconnect",
            "option_c": "1. Ping -> 2. Echo -> 3. Trace -> 4. Route",
            "option_d": "1. SYN -> 2. SYN-ACK -> 3. ACK -> 4. DATA",
            "answer": "A",
            "explanation": "DHCP DORA sequence: Client broadcasts Discover (UDP 67/68); Server responds with Offer; Client broadcasts Request (confirming chosen lease); Server responds with Pack ACK (binding IP/mask/gateway/DNS).",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "SNMP",
            "question": "In Simple Network Management Protocol (SNMPv2c/SNMPv3), what is a 'Trap' message?",
            "option_a": "An unprompted, asynchronous notification message sent by an SNMP agent on a managed network device to the SNMP Manager alerting of critical events (e.g. link down, high temp)",
            "option_b": "A cyberattack that disables network routers",
            "option_c": "A synchronous poll query asking for interface bandwidth",
            "option_d": "A command that reboots the core switch",
            "answer": "A",
            "explanation": "While most SNMP is manager-initiated polling (GetRequest), SNMP Traps/Informs are agent-initiated push alerts sent to UDP port 162 when exceptional threshold events occur.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "FTP",
            "question": "Why does File Transfer Protocol (FTP) require two distinct network connections simultaneously for file transfer?",
            "option_a": "A Control Connection (port 21) for commands/status codes that remains open throughout the session, and dynamic Data Connections (port 20 or passive ports) spawned for each file transfer",
            "option_b": "One connection is for download and the other is for upload",
            "option_c": "One connection is for IPv4 and the other is for IPv6",
            "option_d": "One connection transmits file names while the other prints paper invoices",
            "answer": "A",
            "explanation": "FTP separates control and data out-of-band: Port 21 manages authentication and commands (USER, PASS, RETR); separate dynamic TCP data connections open on-demand to stream file bytes.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "TELNET",
            "question": "Why has TELNET (port 23) been completely deprecated in favor of SSH (Secure Shell - port 22) across enterprise networks?",
            "option_a": "TELNET transmits all terminal session data, including root administrative usernames and passwords, in unencrypted plaintext vulnerable to network packet sniffing",
            "option_b": "TELNET cannot run on Linux servers",
            "option_c": "TELNET requires optical fiber cables exclusively",
            "option_d": "TELNET is limited to a maximum speed of 100 baud",
            "answer": "A",
            "explanation": "TELNET transmits plaintext unencrypted ASCII bytes over TCP, allowing any eavesdropper with Wireshark to capture credentials. SSH secures sessions with strong asymmetric/symmetric cryptography.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Google DNS",
            "question": "What are the globally recognized public anycast IP addresses for Google Public DNS?",
            "option_a": "`8.8.8.8` and `8.8.4.4` (IPv4) / `2001:4860:4860::8888` and `2001:4860:4860::8844` (IPv6)",
            "option_b": "`1.1.1.1` and `1.0.0.1`",
            "option_c": "`192.168.1.1` and `192.168.0.1`",
            "option_d": "`127.0.0.1` and `0.0.0.0`",
            "answer": "A",
            "explanation": "Google Public DNS operates anycast resolvers on `8.8.8.8` and `8.8.4.4` (`2001:4860:4860::8888/8844`), routing queries to the nearest geographic data center via BGP anycast.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "POP3",
            "question": "In POP3 (Post Office Protocol version 3), what happens by default when an email client downloads messages from the mail server?",
            "option_a": "Messages are downloaded to local client storage and deleted from the remote mail server, making multi-device synchronization problematic compared to IMAP",
            "option_b": "Messages are encrypted and broadcast to all users on the domain",
            "option_c": "Messages remain synchronized in cloud folders across all devices",
            "option_d": "The mail server deletes the user's account",
            "answer": "A",
            "explanation": "POP3 follows a store-and-forward download-and-delete model designed for single offline computers. IMAP stores mail on server folders, allowing synchronized access across multiple devices.",
            "difficulty": "easy",
            "question_type": "conceptual"
        }
    ]
    for q in s6_m5:
        q.update({"id": q_id, "subject": s_name, "subject_code": s_code, "module": m5_name, "module_number": 5})
        questions.append(q)
        q_id += 1

    # S6 M6: Emerging & Advanced Topics
    m6_name = "Module VI - Emerging & Advanced Topics"
    s6_m6 = [
        {
            "topic": "SDN",
            "question": "What is the defining architectural paradigm of Software-Defined Networking (SDN)?",
            "option_a": "Decoupling the network Control Plane (routing decision intelligence) from the Data Plane (packet forwarding hardware), centralizing control in a programmable software controller",
            "option_b": "Replacing all Ethernet cables with software emulators",
            "option_c": "Running routing protocols inside web browser tabs",
            "option_d": "Eliminating all switches and routers from data centers",
            "answer": "A",
            "explanation": "SDN separates the Control Plane (path computation, policy) from Data Plane switches (fast hardware packet forwarding), managing the entire network via centralized API controllers.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "OpenFlow",
            "question": "In Software-Defined Networking, what role does the OpenFlow protocol serve?",
            "option_a": "It is the standardized southbound interface protocol enabling the centralized SDN Controller to program flow forwarding tables in Data Plane switches",
            "option_b": "It is a graphical web browser for viewing HTML pages",
            "option_c": "It is an operating system for smartphones",
            "option_d": "It is a hardware power supply standard",
            "answer": "A",
            "explanation": "OpenFlow (ONF standard) is the southbound API between controller and switches, allowing the controller to add, update, and delete flow table entries (match fields, priority, actions).",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "NFV",
            "question": "How does Network Functions Virtualization (NFV) transform traditional telecommunication infrastructure?",
            "option_a": "It replaces proprietary dedicated hardware appliances (firewalls, routers, load balancers, EPC) with software Virtual Network Functions (VNFs) running on standard commodity servers/hypervisors",
            "option_b": "It eliminates the need for software code in telecommunications",
            "option_c": "It requires all network traffic to be printed on paper logs",
            "option_d": "It replaces cloud computing with physical landline switches",
            "answer": "A",
            "explanation": "NFV virtualizes L4-L7 network services (firewalls, NAT, IDS/IPS, BRAS) as software VMs or containers on commercial off-the-shelf (COTS) x86 servers, reducing CapEx/OpEx and accelerating service rollout.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Fat Tree",
            "question": "In modern cloud Data Center Networks (DCN), why is the Fat-Tree (multi-rooted Clos) topology widely deployed over traditional 3-tier hierarchical tree architectures?",
            "option_a": "It provides bisection bandwidth scaling and multiple equal-cost parallel paths between any server pair, eliminating core switch oversubscription bottlenecks using ECMP",
            "option_b": "It uses a single giant core router to handle 100% of global internet traffic",
            "option_c": "It is strictly for home Wi-Fi networks",
            "option_d": "It requires zero network cables",
            "answer": "A",
            "explanation": "Fat-Tree topologies interconnect commodity switches in a Clos network, providing non-blocking 1:1 bisection bandwidth: as you go up the tree, link capacity increases (thicker branches) to prevent bottlenecks.",
            "difficulty": "hard",
            "question_type": "architecture"
        },
        {
            "topic": "VPN",
            "question": "What protocols and modes are utilized in IPsec (Internet Protocol Security) to provide both confidentiality (encryption) and data integrity/authentication for secure VPN tunnels?",
            "option_a": "Encapsulating Security Payload (ESP) in Tunnel Mode with IKE (Internet Key Exchange) for automated key negotiation",
            "option_b": "HTTP in plaintext mode over TCP port 80",
            "option_c": "Simple Telnet commands without encryption",
            "option_d": "FTP in anonymous mode",
            "answer": "A",
            "explanation": "IPsec VPNs use ESP (protocol 50) for encryption and integrity, AH (protocol 51) for authentication, and IKE/ISAKMP (UDP 500) for key exchange; Tunnel Mode encrypts the entire original IP packet.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "SD-WAN",
            "question": "What is the primary enterprise business advantage of Software-Defined Wide Area Networking (SD-WAN) over legacy MPLS circuits?",
            "option_a": "It dynamically steers traffic across hybrid transport links (MPLS, broadband fiber, 5G LTE) based on real-time application QoS requirements, reducing WAN bandwidth costs",
            "option_b": "It eliminates the need for internet service providers",
            "option_c": "It requires all branch offices to use dial-up modems",
            "option_d": "It prohibits remote employees from accessing cloud applications",
            "answer": "A",
            "explanation": "SD-WAN decouples network hardware from control mechanism, using software overlays to route traffic intelligently across cheap commercial broadband and MPLS based on latency, jitter, and packet loss.",
            "difficulty": "medium",
            "question_type": "application"
        },
        {
            "topic": "SDN controllers",
            "question": "Which of the following represents widely deployed open-source SDN Controllers used in carrier and enterprise networks?",
            "option_a": "OpenDaylight (ODL) and ONOS (Open Network Operating System)",
            "option_b": "Microsoft Word and Adobe Photoshop",
            "option_c": "Apache Tomcat and Nginx",
            "option_d": "MySQL and MongoDB",
            "answer": "A",
            "explanation": "OpenDaylight (ODL) and ONOS are prominent modular, open-source SDN controller platforms written in Java, featuring rich northbound REST APIs and southbound OpenFlow/NETCONF drivers.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Data Center Networks",
            "question": "In modern hyperscale cloud data centers (East-West traffic between servers), what protocol replaced legacy Spanning Tree Protocol (STP) to enable multi-path active-active forwarding?",
            "option_a": "Equal-Cost Multi-Path (ECMP) routing across Layer 3 Spine-and-Leaf fabrics and VXLAN overlays",
            "option_b": "Single-threaded CSMA/CD",
            "option_c": "Pure ALOHA radio broadcasting",
            "option_d": "Token Ring token passing",
            "answer": "A",
            "explanation": "Spanning Tree blocks redundant links to prevent loops, wasting 50% of bandwidth. Spine-Leaf fabrics use Layer 3 ECMP and VXLAN to keep all physical links active simultaneously.",
            "difficulty": "hard",
            "question_type": "architecture"
        },
        {
            "topic": "VPN types",
            "question": "What is the difference between a Site-to-Site VPN and a Remote-Access VPN?",
            "option_a": "Site-to-Site connects two permanent office network locations over encrypted gateway tunnels; Remote-Access connects individual mobile workers to the corporate network via client software",
            "option_b": "Site-to-Site is only for home users while Remote-Access is for data centers",
            "option_c": "Remote-Access requires digging physical fiber cables to every employee's house",
            "option_d": "Site-to-Site does not use encryption",
            "answer": "A",
            "explanation": "Site-to-site VPNs connect branch gateways (transparent to users on local LANs); remote-access VPNs (SSL/TLS or IPsec client) authenticate roaming individuals to the corporate intranet.",
            "difficulty": "easy",
            "question_type": "comparison"
        },
        {
            "topic": "NFV benefits",
            "question": "What are the primary operational benefits achieved by telecom operators adopting Network Functions Virtualization (NFV)?",
            "option_a": "Reduced Capital Expenditure (CapEx) and Operating Expenditure (OpEx), rapid automated service provisioning, dynamic elasticity/auto-scaling, and simplified hardware maintenance",
            "option_b": "Elimination of all software licenses and customer billing",
            "option_c": "Replacing all digital fiber with analog copper cables",
            "option_d": "Increasing physical server footprint in central offices by 500%",
            "answer": "A",
            "explanation": "NFV eliminates vendor-locked specialized hardware, allowing carriers to spin up virtual firewalls or 5G Core user planes in minutes on standard cloud hardware with automated scaling.",
            "difficulty": "easy",
            "question_type": "conceptual"
        }
    ]
    for q in s6_m6:
        q.update({"id": q_id, "subject": s_name, "subject_code": s_code, "module": m6_name, "module_number": 6})
        questions.append(q)
        q_id += 1

    return questions, q_id

def generate_s7_questions(start_id):
    # Subject 7: Indian Knowledge System (2015511)
    s_name = "Indian Knowledge System"
    s_code = "2015511"
    q_id = start_id
    questions = []

    # S7 M1: Acoustic Science in Vedic Chanting and Indian Music
    m1_name = "Module I - Acoustic Science in Vedic Chanting and Indian Music"
    s7_m1 = [
        {
            "topic": "Shruti",
            "question": "In classical Indian musicology and acoustic science (as formalized in Bharata's Natyashastra and Sarangadeva's Sangita Ratnakara), how many microtonal intervals ('Shrutis') are identified within a single octave (Saptak)?",
            "option_a": "22 Shrutis",
            "option_b": "12 Shrutis",
            "option_c": "7 Shrutis",
            "option_d": "64 Shrutis",
            "answer": "A",
            "explanation": "The 22-Shruti system divides the octave into 22 acoustically distinct microtonal intervals based on just intonation harmonic ratios (e.g. 9/8, 10/9, 16/15), enabling subtle raga inflections.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Nāda",
            "question": "In Indian acoustic philosophy, what is the foundational distinction between 'Āhata Nāda' and 'Anāhata Nāda'?",
            "option_a": "Āhata Nāda is struck, physical audible sound produced by mechanical vibration and medium friction; Anāhata Nāda is unstruck, primordial cosmic vibration realized through deep meditation",
            "option_b": "Āhata Nāda is electronic audio while Anāhata Nāda is radio waves",
            "option_c": "Āhata Nāda is noise pollution while Anāhata Nāda is spoken language",
            "option_d": "Both refer strictly to ultrasonic medical scanning waves",
            "answer": "A",
            "explanation": "Indian acoustic texts classify sound into Āhata (struck/manifested sound in physical acoustic physics) and Anāhata (unstruck/unmanifested primordial vibration of consciousness).",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Pitch",
            "question": "In Vedic chanting phonetics (Shiksha Vedanga), what are the three primary pitch accents (Svaras) that govern the semantic meaning of recited mantras?",
            "option_a": "Udātta (high/raised pitch), Anudātta (low/unraised pitch), and Svarita (circumflex/falling modulated pitch)",
            "option_b": "Sa, Re, Ga",
            "option_c": "Hrasva, Dirgha, Pluta",
            "option_d": "Tivra, Komal, Shuddha",
            "answer": "A",
            "explanation": "Vedic recitation is strictly tonal/pitch-accented: Udātta (elevated pitch), Anudātta (base pitch), and Svarita (falling transition). Shifting pitch alters the grammatical meaning of the text.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Harmonic content",
            "question": "In acoustic analysis of Indian musical instruments like the Tanpura (Tambura), what acoustic mechanism creates the rich, shimmering overtones known as the 'Javari' (buzzing bridge)?",
            "option_a": "Non-linear string-bridge grazing contact over a curved wide bridge with a cotton thread, continuously transferring energy into high-frequency harmonic overtones",
            "option_b": "Electronic synthesizer distortion amplifiers inside the wooden gourd",
            "option_c": "Using nylon guitar strings tuned to random frequencies",
            "option_d": "A vacuum tube pre-amplifier embedded in the neck",
            "answer": "A",
            "explanation": "The Javari thread on a wide curved bridge causes dynamic boundary conditions: string length changes cyclically during vibration, exciting a dense spectrum of non-linear overtone harmonics.",
            "difficulty": "hard",
            "question_type": "conceptual"
        },
        {
            "topic": "Indian acoustic practices",
            "question": "In the acoustic design of ancient Indian temple sanctums (Garbhagriha) and Natyamandapas, how do stone geometry and pillared colonnades influence sound reverberation?",
            "option_a": "Specific stone material densities and geometric proportions enhance low-frequency vocal resonance (chanting) while scattering flutter echoes to maintain vocal clarity",
            "option_b": "By absorbing 100% of all sound waves to create absolute silence",
            "option_c": "By converting sound waves into electrical power",
            "option_d": "By generating artificial electronic reverberation effects",
            "answer": "A",
            "explanation": "Temple acoustics (e.g. at Madurai or Thanjavur) utilize resonant granite chambers and carved acoustic diffusion pillars to optimize human voice resonance and chant clarity.",
            "difficulty": "medium",
            "question_type": "application"
        },
        {
            "topic": "22 microtones",
            "question": "In Bharata's famous 'Sarana Chatushtayi' experiment using two identical 22-string harps (Achala Vina and Chala Vina), what was demonstrated?",
            "option_a": "The empirical derivation and physical verification of all 22 distinct Shruti intervals through 4 successive tuning shift iterations",
            "option_b": "The measurement of the speed of light in vacuum",
            "option_c": "The proof of the Pythagorean theorem using geometry",
            "option_d": "The discovery of radio electromagnetic waves",
            "answer": "A",
            "explanation": "Bharata's Sarana Chatushtayi kept one Vina fixed (Achala) while retuning the other (Chala) through 4 microtonal shifts, proving the exact ratios (Pramana Shruti approx 81/80) of all 22 Shrutis.",
            "difficulty": "hard",
            "question_type": "conceptual"
        },
        {
            "topic": "Frequency discrimination",
            "question": "How does Vedic chanting training enhance psychoacoustic auditory frequency discrimination in modern cognitive science studies?",
            "option_a": "Rigorous phonetic training in precise articulation places (Sthāna) and microtonal pitch control strengthens neuroplasticity in auditory cortex frequency tuning",
            "option_b": "By surgically altering the physical shape of the ear canal",
            "option_c": "By listening exclusively to white noise audio tracks",
            "option_d": "By completely eliminating the brain's temporal processing lobes",
            "answer": "A",
            "explanation": "Studies (e.g. by neuroscientists studying the 'Sanskrit Effect') show Vedic chanters exhibit superior auditory processing, precise pitch discrimination, and enlarged memory-associated cortical regions.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Sound",
            "question": "According to Paninian phonetics (Paniniya Shiksha), what is the physiological sequence of sound production in the human body?",
            "option_a": "Soul/Mind inspires the intellect -> mind strikes the internal bodily fire (Kāyāgni) -> air (Prāna) is driven up through chest, throat, head, and articulated by oral organs",
            "option_b": "Lungs pump air directly without nervous system involvement",
            "option_c": "Sound originates entirely in the ear canal and radiates outward",
            "option_d": "Sound is produced by mechanical teeth grinding alone",
            "answer": "A",
            "explanation": "Paniniya Shiksha (verses 6-9) details the bio-acoustic mechanism: consciousness conceives meaning, intellect directs mind, mind activates breath (Vāyu), modulated through 8 articulation places.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Frequency",
            "question": "What is the relationship between the fundamental tonic note 'Shadja' (Sa) and 'Panchama' (Pa) in Indian musical acoustics (the Shadja-Panchama Bhāva)?",
            "option_a": "A perfect fifth interval with frequency ratio 3:2 (1.50 times the frequency of Sa)",
            "option_b": "A frequency ratio of 2:1 (an octave)",
            "option_c": "A frequency ratio of 4:3 (Shadja-Madhyama Bhāva)",
            "option_d": "Two completely identical unison frequencies",
            "answer": "A",
            "explanation": "Shadja-Panchama Bhāva (Samvādi consonant relationship) represents the acoustic pure fifth ratio 3/2 (e.g. Sa = 240 Hz, Pa = 360 Hz), providing the foundational consonance of Indian music.",
            "difficulty": "easy",
            "question_type": "numerical"
        },
        {
            "topic": "Indian acoustic practices",
            "question": "In the acoustic design of Indian percussion instruments like the Mridangam and Tabla, what is the role of the central black tuning paste ('Siyahi' / 'Karanai')?",
            "option_a": "It applies non-uniform mass loading to the multi-layered leather membrane, suppressing inharmonic Bessel function overtones to produce clear harmonic, pitch-centered musical tones",
            "option_b": "It is purely decorative black paint with zero acoustic impact",
            "option_c": "It prevents the drum from slipping off the player's lap",
            "option_d": "It absorbs all moisture to make the drum completely silent",
            "answer": "A",
            "explanation": "Nobel Laureate Sir C.V. Raman proved (1920) that circular membranes naturally have inharmonic overtones; the metallic iron-paste Siyahi loads the center, transforming modes into harmonic integer ratios (1:2:3:4).",
            "difficulty": "hard",
            "question_type": "conceptual"
        }
    ]
    for q in s7_m1:
        q.update({"id": q_id, "subject": s_name, "subject_code": s_code, "module": m1_name, "module_number": 1})
        questions.append(q)
        q_id += 1

    # S7 M2: Indian Knowledge and Sustainable/Renewable Energy
    m2_name = "Module II - Indian Knowledge and Sustainable/Renewable Energy"
    s7_m2 = [
        {
            "topic": "Ancient Indian energy practices",
            "question": "In ancient Indian town planning and architecture (Vāstu Shāstra), how was passive solar architecture integrated into building orientations?",
            "option_a": "Buildings were oriented along cardinal solar axes with central courtyards (Brahmasthana) and shading verandas to maximize natural daylighting and stack-effect passive ventilation",
            "option_b": "By constructing completely windowless underground concrete bunkers",
            "option_c": "By painting all exterior walls pitch black in tropical regions",
            "option_d": "By relying exclusively on coal-fired electrical boilers",
            "answer": "A",
            "explanation": "Vastu Shastra and traditional haveli architecture employ courtyard thermal chimneys (Brahmasthana), thick thermal mass walls, and orientation to catch prevailing breezes and solar paths.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Traditional energy systems",
            "question": "What is the traditional 'Ahar-Pyne' system of ancient Magadh (Bihar) and what sustainable water-energy management function does it serve?",
            "option_a": "An indigenous community-managed rainwater harvesting and floodwater diversion canal-reservoir system providing gravity-driven agricultural irrigation without mechanical pumps",
            "option_b": "A method for smelting high-carbon wootz steel",
            "option_c": "A mathematical formula for calculating eclipse cycles",
            "option_d": "A system of steam-powered locomotives",
            "answer": "A",
            "explanation": "The Ahar-Pyne system captures flash floods from hilly rivers into retention reservoirs (Ahars) via diversion channels (Pynes), utilizing natural elevation contours for zero-energy gravity irrigation.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Sustainability",
            "question": "In the Ishavasya Upanishad, what fundamental ecological philosophy is expressed in the phrase 'Īśā vāsyam idaṁ sarvam... mā gṛdhaḥ kasya svid dhanam'?",
            "option_a": "Everything in the universe is pervaded by the Divine; enjoy resources with restraint and renunciation, without coveting what belongs to others (sustainable consumption)",
            "option_b": "Extract all natural mineral resources as quickly as possible for profit",
            "option_c": "Nature exists solely for unconstrained human exploitation",
            "option_d": "Human technology is completely separate from environmental biology",
            "answer": "A",
            "explanation": "This Upanishadic aphorism forms the ethical cornerstone of Indian ecological sustainability: recognizing sacred interconnectedness of nature and practicing restraint/non-greed in resource usage.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Renewable energy knowledge",
            "question": "In ancient Indian architectural texts like the Mayamata and Manasara, how did the design of 'Stepwells' (Bawdis/Vavs) in arid regions achieve natural geothermal cooling?",
            "option_a": "Subterranean subterranean depth and water evaporation lowered ambient subterranean air temperatures by 5-10 degrees Celsius, creating cool microclimatic community refuges",
            "option_b": "By installing electric air conditioning compressors underground",
            "option_c": "By burning charcoal at the bottom of the well",
            "option_d": "By lining well walls with lead sheets",
            "answer": "A",
            "explanation": "Stepwells (like Rani ki Vav) combine water conservation with passive geothermal cooling: subterranean thermal inertia and evaporative cooling create comfortable ambient microclimates.",
            "difficulty": "easy",
            "question_type": "application"
        },
        {
            "topic": "Modern engineering interpretation",
            "question": "How can traditional Indian 'Surkhi' (calcined clay pozzolan mortar) and lime plasters be interpreted in modern low-carbon green building engineering?",
            "option_a": "As low-carbon, breathable bio-cementitious alternatives that reduce the heavy carbon footprint and embodied energy associated with modern Ordinary Portland Cement (OPC)",
            "option_b": "As radioactive industrial waste materials",
            "option_c": "As non-recyclable toxic polymers",
            "option_d": "As expensive synthetic chemical adhesives",
            "answer": "A",
            "explanation": "Traditional lime-surkhi mortars have low embodied carbon, excellent durability over centuries, self-healing calcification properties, and superior thermal insulation compared to Portland cement.",
            "difficulty": "medium",
            "question_type": "application"
        },
        {
            "topic": "Ancient Indian energy practices",
            "question": "In the Arthashastra of Kautilya, what strict administrative regulations governed forest management and wildlife conservation?",
            "option_a": "Classification into productive economic forests (Dravya-vana), elephant sanctuaries (Hasti-vana), and protected reserves (Abhayaranya) with severe penalties for unauthorized felling or poaching",
            "option_b": "Mandating complete clear-cutting of all forests for urban sprawl",
            "option_c": "Prohibiting agriculture across all fertile river valleys",
            "option_d": "Selling all forest land to private foreign merchants",
            "answer": "A",
            "explanation": "Kautilya established sophisticated state forestry departments headed by the Kupyadhyaksha, establishing protected wildlife sanctuaries (Abhayaranya) and sustainable harvesting cycles.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Traditional energy systems",
            "question": "What is the 'Kuhl' system of gravity irrigation developed in the western Himalayan valleys (Himachal Pradesh)?",
            "option_a": "Community-engineered contour surface channels that transport melting glacial stream runoff along steep mountain ridges to terraced agricultural fields using zero fossil energy",
            "option_b": "Diesel-powered high-pressure water pumps",
            "option_c": "Deep underground oil drilling rigs",
            "option_d": "Nuclear-powered desalination plants",
            "answer": "A",
            "explanation": "Kuhls are traditional gravity-fed channels tapping glacial streams high in the Himalayas, distributing water across steep terraced fields through cooperative community management (Kohli).",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Sustainability",
            "question": "How did the traditional concept of 'Panchabhuta' (Earth, Water, Fire, Air, Space) guide resource equilibrium in ancient Indian life sciences (Ayurveda and Vrikshayurveda)?",
            "option_a": "All material manifestations are dynamic balances of the five primal elements; disruption of any elemental cycle causes environmental illness and ecological degradation",
            "option_b": "By treating physical matter as purely economic commodities",
            "option_c": "By rejecting the physical laws of thermodynamics",
            "option_d": "By defining energy as a static non-transformable quantity",
            "answer": "A",
            "explanation": "The Panchabhuta framework establishes that human health and ecological health are identical systems governed by harmonious equilibrium of the 5 elements (Bhutas).",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Modern engineering interpretation",
            "question": "What sustainable principle from traditional Indian agriculture (Krishi Parashara / Vrikshayurveda) is applied in modern Organic Zero Budget Natural Farming (ZBNF)?",
            "option_a": "Using fermented microbial soil inoculants (Jeevamrutha / Beejamrutha) prepared from native cow dung and urine to restore biological soil microbiome without synthetic chemical fertilizers",
            "option_b": "Heavy aerial spraying of chlorinated chemical pesticides",
            "option_c": "Excessive flood irrigation leading to soil salinization",
            "option_d": "Burning crop residue and clearing topsoil with chemicals",
            "answer": "A",
            "explanation": "Vrikshayurveda techniques (Kunapajala / Beejamrutha) revitalize soil biology via beneficial microbial consortia, reducing input costs and preserving groundwater quality sustainably.",
            "difficulty": "medium",
            "question_type": "application"
        },
        {
            "topic": "Ancient Indian energy practices",
            "question": "What metallurgical property of the 1,600-year-old Iron Pillar of Delhi demonstrates advanced ancient Indian sustainable materials engineering?",
            "option_a": "Exceptional resistance to atmospheric corrosion due to high phosphorus content forming a protective crystalline iron hydrogen phosphate hydrate (misawite) film",
            "option_b": "It is coated in modern synthetic epoxy paint",
            "option_c": "It is made of pure stainless steel imported from Europe",
            "option_d": "It is maintained inside an airtight vacuum chamber",
            "answer": "A",
            "explanation": "IIT Kanpur metallurgical studies confirmed that ancient forge-welded high-phosphorus wrought iron catalytically formed a protective passive film (Misawite), preventing rust for over 16 centuries.",
            "difficulty": "hard",
            "question_type": "case_study"
        }
    ]
    for q in s7_m2:
        q.update({"id": q_id, "subject": s_name, "subject_code": s_code, "module": m2_name, "module_number": 2})
        questions.append(q)
        q_id += 1

    # S7 M3, M4, M5, M6
    s7_m3_name = "Module III - Linguistics, Number Systems and Rainfall Prediction"
    s7_m3 = [
        {
            "topic": "Pingala",
            "question": "In the Chandas Shastra (circa 300-200 BCE), what foundational computer science concepts did the Indian mathematician-prosodist Pingala formulate when analyzing poetic meters (Laghu and Guru syllables)?",
            "option_a": "The Binary Number System (Dvyaṅka), Meru Prastāra (Pascal's Triangle), and Binomial Coefficients",
            "option_b": "Object-Oriented Programming and Virtual Memory",
            "option_c": "Relational Database Normalization",
            "option_d": "TCP/IP Packet Routing",
            "answer": "A",
            "explanation": "Pingala mapped light (Laghu=0) and heavy (Guru=1) syllables, developing binary representations, combinatorial permutations (Prastāra), and the binomial triangle (Meru Prastāra).",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Katapayadi",
            "question": "In the Katapayadi alphanumeric encryption system developed in ancient India, how are Sanskrit consonants mapped to decimal digits (0-9)?",
            "option_a": "Consonants beginning with Ka, Ta, Pa, Ya map to digit 1, with successive consonants mapping sequentially up to 9 and 0 (vowels are ignored)",
            "option_b": "Each letter maps to its ASCII binary byte value",
            "option_c": "Vowels represent prime numbers while consonants represent negative numbers",
            "option_d": "All letters map to the digit 5",
            "answer": "A",
            "explanation": "Katapayadi system: Ka=1..Jha=9, Nya=0; Ta=1..Dha=9, Na=0; Pa=1..Ma=5; Ya=1..Ha=8. Read right-to-left ('aṅkānāṁ vāmato gatiḥ'), encoding mathematical constants into memorable verses.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Pāṇini",
            "question": "Why is Pāṇini's grammatical treatise 'Ashtadhyayi' (circa 500 BCE) considered the world's first formal generative language system and a direct precursor to modern computer science context-free grammars (BNF)?",
            "option_a": "It defines Sanskrit using an algebraic meta-language with ~4,000 algorithmic production rules, auxiliary markers (It-markers), recursion, and strict rule precedence (Sutra ordering)",
            "option_b": "It was compiled using a C++ compiler",
            "option_c": "It is a dictionary containing list of English words",
            "option_d": "It has no formal mathematical rules",
            "answer": "A",
            "explanation": "Panini's grammar is a Turing-complete formal generative system: utilizing concise production rules, auxiliary markers (like non-terminals in Backus-Naur Form BNF), and algorithmic conflict resolution.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Sanskrit NLP",
            "question": "Why did Rick Briggs (NASA AI researcher, 1985) publish the landmark paper 'Knowledge Representation in Sanskrit and Artificial Intelligence' advocating Sanskrit for AI semantic representation?",
            "option_a": "Because Sanskrit's unambiguous morphological case inflections (Vibhaktis) and explicit semantic role structures (Kāraka theory) map directly to semantic networks without structural ambiguity",
            "option_b": "Because Sanskrit has no grammar rules",
            "option_c": "Because computers in 1985 could only process Sanskrit text",
            "option_d": "Because Sanskrit words can only have 1 meaning",
            "answer": "A",
            "explanation": "Briggs demonstrated that Paninian Karaka analysis represents exact semantic dependencies between sentence entities regardless of word order, acting as an unambiguous natural language knowledge graph.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Panchang",
            "question": "What are the five astronomical attributes ('Panchangas') that constitute the traditional Indian lunisolar calendar?",
            "option_a": "Tithi (lunar day), Vāra (weekday), Nakshatra (lunar mansion), Yoga (soli-lunar sum angle), and Karana (half tithi)",
            "option_b": "Hour, Minute, Second, Millisecond, Microsecond",
            "option_c": "Mercury, Venus, Mars, Jupiter, Saturn",
            "option_d": "Spring, Summer, Monsoon, Autumn, Winter",
            "answer": "A",
            "explanation": "Panchanga (5 limbs of time): Tithi (12-degree moon-sun separation), Vara (solar day of week), Nakshatra (13 deg 20 min lunar asterism), Yoga (combined longitude), and Karana (6-degree half-tithi).",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Nakshatras",
            "question": "In the Indian astronomical ecliptic division, into how many equal Nakshatras (lunar mansions) is the 360-degree zodiac partitioned, and what is the angular span of each?",
            "option_a": "27 Nakshatras; each spanning exactly 13 degrees 20 minutes (800 arcminutes)",
            "option_b": "12 Nakshatras; each spanning 30 degrees",
            "option_c": "360 Nakshatras; each spanning 1 degree",
            "option_d": "7 Nakshatras; each spanning 51.4 degrees",
            "answer": "A",
            "explanation": "The 360-degree ecliptic is divided into 27 Nakshatras of 13°20' each (further subdivided into 4 Padas of 3°20' each, totaling 108 Padas), tracking the Moon's sidereal orbital progression.",
            "difficulty": "medium",
            "question_type": "numerical"
        },
        {
            "topic": "Traditional rainfall indicators",
            "question": "In the meteorological traditions of Varāhamihira (Brihat Samhita) and Krishi Parashara, what is the 'Garbhadhāna' (conception of clouds) theory of rainfall forecasting?",
            "option_a": "Atmospheric conditions, wind directions, and cloud formations observed during specific lunar asterisms approximately 195 days (6.5 solar months) prior to rain indicate monsoon precipitation strength",
            "option_b": "Rainfall occurs purely at random without any seasonal patterns",
            "option_c": "Clouds are formed by underground earthquakes exclusively",
            "option_d": "Rainfall can only occur on Tuesdays",
            "answer": "A",
            "explanation": "Varahamihira documented 'Garbhadhana' (cloud foetus formation): specific atmospheric indicators (temperature, halos, wind vectors) during winter gestational months correlate with monsoon yields 195 days later.",
            "difficulty": "hard",
            "question_type": "conceptual"
        },
        {
            "topic": "Decimal system",
            "question": "What three mathematical components invented in ancient India revolutionized global computational mathematics?",
            "option_a": "Decimal base-10 numeration, the concept and symbol for Zero (Shunya) as both a placeholder and an operational number, and Positional Place Value",
            "option_b": "Roman numerals, Abacus rods, and Tally sticks",
            "option_c": "Hexadecimal base-16 exclusively",
            "option_d": "Non-Euclidean hyperbolic space coordinates",
            "answer": "A",
            "explanation": "The Indian decimal place-value system with zero (as praised by Laplace and Severus Sebokht) allowed all arithmetic operations to be expressed concisely with 10 symbols, enabling modern computational science.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Natural indicators",
            "question": "In traditional Indian rural ethno-meteorology, which bio-indicators are traditionally monitored to anticipate immediate rainfall arrival?",
            "option_a": "Unusual behavioral changes in animals/insects (e.g. ants moving eggs upward, dragonflies swarming low, frogs croaking persistently) due to barometric pressure and humidity shifts",
            "option_b": "Sudden drop in computer CPU clock speed",
            "option_c": "Changes in radio station broadcast frequencies",
            "option_d": "Magnetic alignment of compass needles pointing South",
            "answer": "A",
            "explanation": "Ethno-meteorological bio-indicators leverage animal sensitivity to acute drops in atmospheric pressure, rising relative humidity, and infrasonic acoustic signals preceding thunderstorm fronts.",
            "difficulty": "easy",
            "question_type": "application"
        },
        {
            "topic": "Binary",
            "question": "In Pingala's combinatorial algorithm 'Prastāra' for expanding all n-syllable meters, how does the generation sequence correspond to modern binary truth tables?",
            "option_a": "It systematically enumerates all 2^n binary combinations of Laghu (0) and Guru (1) in a precise recursive bit-reversal lexicographic order",
            "option_b": "It only generates odd numbers",
            "option_c": "It randomly picks syllables without order",
            "option_d": "It can only evaluate n = 1",
            "answer": "A",
            "explanation": "Pingala's Prastāra rule systematically generates the complete binary tree of 2^n permutations for n-bit strings, identical to modern binary Gray-code or truth table enumeration.",
            "difficulty": "hard",
            "question_type": "conceptual"
        }
    ]
    for q in s7_m3:
        q.update({"id": q_id, "subject": s_name, "subject_code": s_code, "module": s7_m3_name, "module_number": 3})
        questions.append(q)
        q_id += 1

    # S7 M4: Mathematics Foundations in Ancient India and Relevance to IT
    s7_m4_name = "Module IV - Mathematics Foundations in Ancient India and Relevance to IT"
    s7_m4 = [
        {
            "topic": "Aryabhata",
            "question": "In the Aryabhatiya (499 CE), what remarkably accurate approximation did Aryabhata compute for the mathematical constant Pi (pi), and what visionary insight did he state?",
            "option_a": "pi approx 62832 / 20000 = 3.1416; stating explicitly that this value is an 'approximation' (āsanna), anticipating irrationality",
            "option_b": "pi = 3.0 exactly",
            "option_c": "pi = 22 / 7 with zero decimal places",
            "option_d": "pi is a negative integer",
            "answer": "A",
            "explanation": "Aryabhata (Ganitapada verse 10) gave: (100+4)*8 + 62000 / 20000 = 62832/20000 = 3.1416, calling it 'asanna' (approaching/approximate), recognizing that circle circumference is incommensurable with diameter.",
            "difficulty": "medium",
            "question_type": "numerical"
        },
        {
            "topic": "Brahmagupta",
            "question": "In the Brahmasphutasiddhanta (628 CE), what fundamental arithmetic rules did Brahmagupta formulate for operations involving Zero and negative numbers ('Debt' / Kṣiṇa)?",
            "option_a": "Negative * Negative = Positive; Positive * Negative = Negative; A number multiplied by Zero is Zero; 0 / 0 = 0 (early exploration of zero arithmetic)",
            "option_b": "Negative numbers do not exist and are prohibited",
            "option_c": "Multiplying two negative numbers produces a negative number",
            "option_d": "Zero cannot be added to any number",
            "answer": "A",
            "explanation": "Brahmagupta formalized complete arithmetic rules for positive numbers (Dhāna/Fortune), negative numbers (Rṇa/Debt), and Zero (Kha/Shunya), establishing modern sign rules.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Algorithmic thinking",
            "question": "What is the 'Kuttaka' (Pulverizer) algorithm developed by Aryabhata and refined by Bhaskara I for solving linear Diophantine equations of the form ax + c = by in integers?",
            "option_a": "A continuous division Euclidean algorithm and recursive backward substitution technique, identical to the modern Extended Euclidean Algorithm used in RSA Cryptography",
            "option_b": "A method for multiplying matrices using GPUs",
            "option_c": "A random guess Monte Carlo procedure",
            "option_d": "A trigonometric table lookup",
            "answer": "A",
            "explanation": "Kuttaka ('pulverizing' coefficients into smaller remainders) solves linear Diophantine equations ax - by = c. Its recursive quotients-remainder ladder is mathematically identical to Extended Euclidean algorithm.",
            "difficulty": "hard",
            "question_type": "conceptual"
        },
        {
            "topic": "Bhaskara II",
            "question": "In the Lilavati and Bijaganita (1150 CE), what algorithm did Bhāskara II invent to solve the indeterminate quadratic equation Nx^2 + 1 = y^2 (erroneously named Pell's Equation by Euler)?",
            "option_a": "The Chakravala (Cyclic) method, a cyclic algorithmic process generating integer solutions centuries before Lagrange",
            "option_b": "The Newton-Raphson tangent line method",
            "option_c": "The Simplex linear programming method",
            "option_d": "Gradient descent backpropagation",
            "answer": "A",
            "explanation": "The Chakravala method (praised by Hermann Hankin and George Gheverghese Joseph) is an optimal cyclic algorithm that computes minimal integer solutions to Nx^2 + 1 = y^2 in finite steps.",
            "difficulty": "hard",
            "question_type": "conceptual"
        },
        {
            "topic": "Modular arithmetic",
            "question": "How is ancient Indian modular arithmetic (Bhavana composition rules and Kuttaka) applied in modern computer cybersecurity and public-key cryptography (e.g. RSA)?",
            "option_a": "In computing modular multiplicative inverses `a^(-1) mod m` and modular exponentiations essential for RSA key generation and Diffie-Hellman key exchange",
            "option_b": "In designing HTML web page colors",
            "option_c": "In cooling data center server fans",
            "option_d": "In compiling CSS style stylesheets",
            "answer": "A",
            "explanation": "Modern asymmetric cryptography (RSA, ECC) relies on modular arithmetic and solving linear modular congruences ax = 1 (mod m), precisely the mathematical domain of Kuttaka.",
            "difficulty": "medium",
            "question_type": "application"
        },
        {
            "topic": "Checksums",
            "question": "What ancient Indian Vedic arithmetic check (Navashesh / Casting out Nines) is used to rapidly verify the integrity of large multiplications?",
            "option_a": "Digital Root checking: taking the sum of digits modulo 9 for operands and product; if DigitalRoot(A * B) != DigitalRoot(Product), an error is detected",
            "option_b": "Subtracting 100 from every number",
            "option_c": "Converting all numbers to Roman numerals",
            "option_d": "Dividing all numbers by 2 and checking if integer",
            "answer": "A",
            "explanation": "Casting out nines (Navashesh) uses modulo 9 properties: since 10 = 1 (mod 9), any integer is congruent to its digit sum mod 9, providing an instantaneous arithmetic parity checksum.",
            "difficulty": "easy",
            "question_type": "numerical"
        },
        {
            "topic": "Cryptography",
            "question": "In the Vātsyāyana Kamasutra (64 Arts / Chatusshasthi Kalas), which art specifically refers to secret writing, ciphers, and cryptographic substitution codes?",
            "option_a": "Mlecchita Vikalpa (the art of secret communication and cipher writing)",
            "option_b": "Natya (dramatic performance)",
            "option_c": "Vastu Vidya (architecture)",
            "option_d": "Takshana (carpentry)",
            "answer": "A",
            "explanation": "Art #44 in the Kamasutra is Mlecchita Vikalpa (cryptography and ciphering), which describes substitution ciphers like Gudhalekhya and Kautiliya secret intelligence ciphers.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Zero",
            "question": "In the Bakhshali Manuscript (radiocarbon dated from 3rd-4th century CE), what historical mathematical notation was discovered?",
            "option_a": "The earliest physical written dot (bindu) symbol used systematically for Zero as both a placeholder and an arithmetic digit",
            "option_b": "The first written English alphabet",
            "option_c": "A printed map of the American continent",
            "option_d": "An electronic circuit diagram",
            "answer": "A",
            "explanation": "Oxford University radiocarbon dating confirmed the Bakhshali birch-bark manuscript contains the oldest recorded dot symbol representing zero (Shunya-bindu).",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Rule-based mathematical procedures",
            "question": "What algorithmic pedagogy is embodied in the 'Sutra' format of Indian mathematical treatises (Sulba Sutras, Lilavati)?",
            "option_a": "Ultra-compressed, mnemonic algorithmic procedure rules that maximize information density, designed for memorization, mental compilation, and step-by-step algorithmic execution",
            "option_b": "Unstructured random poetry with no mathematical meaning",
            "option_c": "Lengthy verbose legal disclaimers",
            "option_d": "Photographic illustrations without text",
            "answer": "A",
            "explanation": "Sutras are algorithmic pseudocode: concise, unambiguous mathematical rules designed for optimal oral transmission and algorithmic application across diverse problem instances.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Aryabhata",
            "question": "What revolutionary astronomical assertion did Aryabhata make regarding the apparent daily motion of the stars in the night sky?",
            "option_a": "The Earth rotates daily on its own spherical axis from West to East, creating the illusion of the celestial sphere rotating around the Earth",
            "option_b": "The Earth is flat and stationary supported by four elephants",
            "option_c": "The stars travel faster than the speed of light",
            "option_d": "The Sun orbits the Moon every 24 hours",
            "answer": "A",
            "explanation": "Aryabhata (Golapada verse 9) used the famous boat metaphor: just as a person in a moving boat sees stationary shore objects moving backward, humans on rotating Earth see stars moving West.",
            "difficulty": "easy",
            "question_type": "conceptual"
        }
    ]
    for q in s7_m4:
        q.update({"id": q_id, "subject": s_name, "subject_code": s_code, "module": s7_m4_name, "module_number": 4})
        questions.append(q)
        q_id += 1

    # S7 M5: Indian Logic and its Applications in IT
    s7_m5_name = "Module V - Indian Logic and its Applications in IT"
    s7_m5 = [
        {
            "topic": "Nyaya logic",
            "question": "In the classical Nyāya school of Indian logic (Nyāya Sūtras of Akṣapāda Gautama), what are the five members (Pañcāvayava) of a formal syllogism?",
            "option_a": "1. Pratijñā (Proposition), 2. Hetu (Reason), 3. Udāharaṇa (Universal rule with Example), 4. Upanaya (Application to instance), 5. Nigamana (Conclusion)",
            "option_b": "1. Major Premise, 2. Minor Premise, 3. Conclusion, 4. Appendix, 5. Index",
            "option_c": "1. If, 2. Else, 3. While, 4. For, 5. Break",
            "option_d": "1. Input, 2. Process, 3. Output, 4. Store, 5. Delete",
            "answer": "A",
            "explanation": "The 5-step Nyaya inference (e.g. 'The hill has fire; because it has smoke; whatever has smoke has fire, like a hearth; this hill is so; therefore this hill has fire') combines deduction and induction.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Knowledge graphs",
            "question": "In Navya-Nyāya logic (formalized by Gangeśa Upādhyāya in Tattvacintāmaṇi), how does its technical relational language anticipate modern Knowledge Graphs and First-Order Ontologies?",
            "option_a": "It decomposes propositions into rigorous triples of Cognition, Qualifier (Prakāra), Qualificand (Viśeṣya), and Limiting Relation (Avacchedaka), preventing semantic ambiguity",
            "option_b": "It uses raster pixel images to represent nouns",
            "option_c": "It prohibits any logical deductions",
            "option_d": "It replaces logic with random chance",
            "answer": "A",
            "explanation": "Navya-Nyaya developed a precise formal symbolic-conceptual language describing relations, absence (Abhāva), and entity qualifiers, providing a rigorous framework for semantic knowledge representation.",
            "difficulty": "hard",
            "question_type": "conceptual"
        },
        {
            "topic": "Chatbots",
            "question": "In designing conversational AI chatbots and NLP dialogue systems for Indian languages, why is Panini's Kāraka theory superior to English-centric Subject-Verb-Object (SVO) dependency parsers?",
            "option_a": "Indian languages have free word order; Karaka theory identifies semantic role dependencies (Kartā, Karma, Karaṇa, Sampradāna, Apādāna, Adhikaraṇa) through noun case endings regardless of sentence word ordering",
            "option_b": "Because chatbots cannot understand grammar rules",
            "option_c": "Because Indian languages have no verbs",
            "option_d": "Because English grammar handles free word order perfectly",
            "answer": "A",
            "explanation": "In Indian languages, words can be ordered flexibly without changing meaning. Karaka theory parses thematic roles via inflectional affixes (Vibhakti), enabling accurate NLP parsing.",
            "difficulty": "medium",
            "question_type": "application"
        },
        {
            "topic": "Indian logic",
            "question": "What is 'Vyāpti' in Nyāya epistemology and logic?",
            "option_a": "The invariable, unconditional universal concomitance or correlation between the probans / sign (Hetu, e.g. smoke) and the probandum (Sādhya, e.g. fire)",
            "option_b": "A logical contradiction that invalidates a statement",
            "option_c": "A random guess with zero certainty",
            "option_d": "A physical measurement of length in meters",
            "answer": "A",
            "explanation": "Vyapti is the universal inductive invariant ('Wherever there is smoke, there is fire') that guarantees validity in the inference (Anumāna) process.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Responsible digital systems",
            "question": "How do Indian ethical frameworks (Dharma, Satya, Ahimsa, Loka-samgraha) inform the development of Responsible AI and digital systems?",
            "option_a": "By establishing that AI deployment must prioritize collective societal welfare (Loka-samgraha), transparent truthfulness (Satya), non-harm to all beings (Ahimsa), and ethical duty (Dharma)",
            "option_b": "By maximizing advertising revenue regardless of societal harm",
            "option_c": "By automating the creation of deepfake disinformation",
            "option_d": "By replacing human accountability with unaccountable black-box bots",
            "answer": "A",
            "explanation": "Indian ethical systems emphasize duty toward planetary welfare (Loka-samgraha) and non-harm, aligning with modern AI ethics pillars of fairness, transparency, and social good.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Knowledge classification",
            "question": "In the Vaisheshika school of philosophy (Kanāda), into what seven ontological categories (Padārthas) is the entire reality of the universe classified?",
            "option_a": "Dravya (Substance), Guṇa (Quality), Karma (Action), Sāmānya (Generality), Viśeṣa (Particularity), Samavāya (Inherence), and Abhāva (Non-existence)",
            "option_b": "Solid, Liquid, Gas, Plasma, Vacuum, Light, Heat",
            "option_c": "Hardware, Software, Firmware, Middleware, Database, Network, Cloud",
            "option_d": "CPU, RAM, ROM, ALU, Register, Cache, Bus",
            "answer": "A",
            "explanation": "Kanada's Vaisheshika Sutra provides a complete ontological taxonomy of all knowable reality across 7 Padarthas, including physical atomic elements and relations.",
            "difficulty": "hard",
            "question_type": "conceptual"
        },
        {
            "topic": "Indian-language digital tools",
            "question": "What is the primary technical role of the Bhashini initiative (National Language Translation Mission) launched by the Government of India?",
            "option_a": "An open AI platform developing foundational speech-to-speech, ASR, OCR, and MT neural models across 22 scheduled Indian languages to break language barriers in digital governance",
            "option_b": "A private video game development studio",
            "option_c": "A hardware factory manufacturing keyboard cables",
            "option_d": "A social media platform for sharing cooking recipes",
            "answer": "A",
            "explanation": "Digital Bhashini trains and deploys open-source AI pipelines (ASR, NMT, TTS) across 22 official Indian languages, making voice-based citizen digital services universally accessible.",
            "difficulty": "easy",
            "question_type": "application"
        },
        {
            "topic": "Decision-making",
            "question": "In the Bhagavad Gita's psychological model of decision-making, what is the hierarchical relationship among Senses (Indriyas), Mind (Manas), Intellect (Buddhi), and Soul (Atman)?",
            "option_a": "The senses are superior to physical body; the mind is superior to senses; the intellect (Buddhi / discerning faculty) is superior to mind; and the Self is supreme",
            "option_b": "The physical body is superior to all intellectual faculties",
            "option_c": "Senses control the intellect with zero conscious feedback",
            "option_d": "Intellect is subordinate to sensory whims",
            "answer": "A",
            "explanation": "Gita 3.42 outlines cognitive hierarchy: Body < Senses < Mind (emotions/desire) < Buddhi (rational discernment/decision-making) < Atman (pure consciousness).",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Language",
            "question": "In the philosophy of language of Bhartrihari (Vākyapadīya), what is the 'Sphota' theory of linguistic comprehension?",
            "option_a": "Meaning is not grasped by summing isolated phonemes sequentially, but flashes into the listener's consciousness as an indivisible, unified holistic burst of semantic cognition (Sphota)",
            "option_b": "Language consists strictly of separate disconnected letters without context",
            "option_c": "Spoken sounds have zero connection to meaning",
            "option_d": "Sentences cannot convey meaning to human listeners",
            "answer": "A",
            "explanation": "Bhartrihari's Sphota theory posits that speech sounds (Dhvani) serve as catalysts to reveal the pre-existing, indivisible semantic whole (Sphota) in the hearer's mind.",
            "difficulty": "hard",
            "question_type": "conceptual"
        },
        {
            "topic": "IKS and modern technology",
            "question": "How does integrating indigenous Indian Knowledge Systems (IKS) into modern AI and Data Science curricula benefit engineering students?",
            "option_a": "It connects advanced modern computing with foundational algorithmic, linguistic, and ethical traditions developed in India, fostering contextual innovation and decolonized engineering thinking",
            "option_b": "It replaces all modern computer programming languages with ancient scripts",
            "option_c": "It prohibits students from using digital computers",
            "option_d": "It requires students to pass civil service exams",
            "answer": "A",
            "explanation": "IKS in NEP 2020 connects rich civilizational contributions in mathematics, linguistics, astronomy, metallurgy, and logic with modern AI, fostering holistic and ethical problem-solving.",
            "difficulty": "easy",
            "question_type": "conceptual"
        }
    ]
    for q in s7_m5:
        q.update({"id": q_id, "subject": s_name, "subject_code": s_code, "module": s7_m5_name, "module_number": 5})
        questions.append(q)
        q_id += 1

    # S7 M6: Sanskrit Grammar and Computational Modules
    s7_m6_name = "Module VI - Sanskrit Grammar and Computational Modules"
    s7_m6 = [
        {
            "topic": "Sandhi",
            "question": "In computational Sanskrit processing, what is 'Sandhi Splitting' (Sandhi Viccheda) and why is it computationally challenging in Sanskrit text processing?",
            "option_a": "Words undergo euphonic phonetic mergers at morpheme and word boundaries (e.g. vidyā + ālaya = vidyālaya); splitting requires resolving non-deterministic combinatorial boundary fusions",
            "option_b": "Splitting words by deleting all vowels automatically",
            "option_c": "Translating Sanskrit sentences into German",
            "option_d": "Converting lowercase letters to uppercase letters",
            "answer": "A",
            "explanation": "Sandhi transforms boundary phonemes (e.g. tat + ca = tacca). Computational Sandhi splitters use finite-state transducers (FST) to segment complex continuous texts into discrete grammatical tokens.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Morphology",
            "question": "In Paninian computational morphology, what is a 'Dhātu' and how are inflected verb forms (Tiṅanta) generated from it?",
            "option_a": "A verbal root (Dhātu) undergoes derivation via specific affixes (Pratyayas), augment prefixes, and Vikaraṇa infixes across 10 Lakāras (tenses/moods) and 3 persons/numbers",
            "option_b": "A Dhātu is a punctuation mark like a comma or period",
            "option_c": "A Dhātu is a database table index",
            "option_d": "A Dhātu is an unchangeable static noun",
            "answer": "A",
            "explanation": "Panini's Dhatupatha catalogs ~2,000 verbal roots. Applying morphological rules, class infixes (Ganas), and 18 Tin affixes generates all regular and irregular conjugated verbal forms.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Rule-based systems",
            "question": "In Panini's grammar engine (Ashtadhyayi), what is the conflict resolution rule 'Vipratisedhe param karyam' (Sutra 1.4.2)?",
            "option_a": "In case of conflict between two rules of equal force applying simultaneously to the same derivation step, the rule that occurs later in the Sutra order takes precedence",
            "option_b": "The earlier rule always wins",
            "option_c": "Both rules are discarded and the program crashes",
            "option_d": "A random rule is chosen by rolling a die",
            "answer": "A",
            "explanation": "Sutra 1.4.2 establishes a fundamental priority mechanism in rule-based derivation: when two rules with equal applicability collide, the posterior rule (param) prevails.",
            "difficulty": "hard",
            "question_type": "conceptual"
        },
        {
            "topic": "Tokenization",
            "question": "Why is tokenization of classical Sanskrit text significantly more complex than tokenization of standard English text?",
            "option_a": "Sanskrit is written with continuous script (Samasa compounding and Sandhi mergers) without explicit whitespace delimiters between conjoined words, requiring deep morphological analysis to tokenize",
            "option_b": "English has no spaces between words",
            "option_c": "Sanskrit text cannot be encoded in UTF-8 Unicode",
            "option_d": "Sanskrit has only 3 total words in its vocabulary",
            "answer": "A",
            "explanation": "Unlike whitespace-delimited languages, Sanskrit texts feature long multi-word compound chains (Samāsas) and phonetic joins (Sandhi), requiring joint segmentation and morphological tagging.",
            "difficulty": "easy",
            "question_type": "comparison"
        },
        {
            "topic": "Parsing",
            "question": "In Sanskrit Computational Linguistics, what is the role of an 'Anvitābhidhāna' vs 'Abhihitānvaya' semantic parsing parser?",
            "option_a": "Two ancient theories of sentence meaning: Anvitābhidhāna holds words convey meaning only as connected in sentence context; Abhihitānvaya holds individual words convey meanings first, which are then connected",
            "option_b": "One parser processes audio while the other processes video",
            "option_c": "One is for compilers while the other is for web servers",
            "option_d": "Both are algorithms for sorting numbers in descending order",
            "answer": "A",
            "explanation": "Prabhakara's Anvitābhidhānavāda (contextual construction) and Kumarila Bhatta's Abhihitānvayavāda (compositional assembly) directly map to top-down vs bottom-up semantic parsing frameworks.",
            "difficulty": "hard",
            "question_type": "conceptual"
        },
        {
            "topic": "Sanskrit structured language",
            "question": "What is the function of the Shiva Sutras (Maheshvara Sutras) at the beginning of Panini's Ashtadhyayi?",
            "option_a": "They organize the phonemes (varnas) of Sanskrit into 14 compact acoustic groups with anubandhas (marker tags), allowing concise condensed reference to phoneme sets (Pratyāhāras like aC for vowels, haL for consonants)",
            "option_b": "They are astronomical star catalogs",
            "option_c": "They describe temple construction formulas",
            "option_d": "They list medicinal Ayurvedic herbs",
            "answer": "A",
            "explanation": "The 14 Shiva Sutras define a compressed indexing scheme: using marker codas, Panini generates 42+ Pratyāhāra shorthand classes (e.g. 'aL' = all phonemes, 'iK' = i, u, r, l), optimizing rule brevity.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Sanskrit digital tools",
            "question": "What capabilities do modern computational platforms like the 'Sanskrit Heritage Site' (Gérard Huet / INRIA) and University of Hyderabad Sanskrit Tools provide?",
            "option_a": "Automated Sandhi splitters, morphological analyzers, noun/verb inflection generators, compound analyzers (Samāsa-chakra), and dependency parse visualizers",
            "option_b": "Hardware semiconductor etching automation",
            "option_c": "Real estate mortgage calculator software",
            "option_d": "Cryptocurrency blockchain miners",
            "answer": "A",
            "explanation": "Huet's Sanskrit Heritage Engine and Amba Kulkarni's UoH tools implement Paninian computational grammars, processing raw Sanskrit text into detailed syntactic and semantic dependency parse trees.",
            "difficulty": "easy",
            "question_type": "application"
        },
        {
            "topic": "Roots",
            "question": "In Paninian linguistics, how are noun stems (Subanta / Prātipadika) derived from verbal roots?",
            "option_a": "By attaching Kṛt (primary derivational) affixes to verbal roots (Dhātu) to form nouns, adjectives, and participles (e.g. kṛ + ta = kṛta)",
            "option_b": "By deleting the root completely",
            "option_c": "By adding English prefixes like 'un-' or 'dis-'",
            "option_d": "By converting the word into binary machine code",
            "answer": "A",
            "explanation": "Nouns and verbal adjectives in Sanskrit are derived productively from verbal roots (Dhatus) via Krt pratyayas (primary affixes) and Taddhita pratyayas (secondary nominal affixes).",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "NLP",
            "question": "In Natural Language Processing for low-resource Indian languages, how does Sanskrit's shared vocabulary (Tatsama and Tadbhava roots) assist multilingual Neural Machine Translation (NMT)?",
            "option_a": "Sanskrit serves as a morphological bridge/pivot language, enabling shared token embeddings and effective cross-lingual zero-shot transfer across Indo-Aryan and Dravidian language families",
            "option_b": "It forces all translation models to delete non-English words",
            "option_c": "It reduces translation speed to zero words per second",
            "option_d": "It requires manual re-typing of all target sentences",
            "answer": "A",
            "explanation": "Over 50-70% of formal vocabulary in major Indian languages shares Sanskrit lexical roots (Tatsama), enabling multilingual tokenizers (like IndicBERT) to share rich cross-lingual semantic representations.",
            "difficulty": "medium",
            "question_type": "application"
        },
        {
            "topic": "Sentence structure",
            "question": "What are the three essential linguistic conditions identified in Indian epistemology for a collection of words to constitute a meaningful sentence (Vākya)?",
            "option_a": "Ākāṅkṣā (Syntactic Expectancy / Valence), Yogyatā (Semantic Compatibility / Plausibility), and Sannidhi / Āsatti (Temporal/Spatial Proximity)",
            "option_b": "Noun, Adjective, Verb",
            "option_c": "Subject, Verb, Object",
            "option_d": "Past, Present, Future",
            "answer": "A",
            "explanation": "Nyaya and Mimamsa mandate 3 conditions for sentence intelligibility: Akanksha (grammatical mutual need of words), Yogyata (semantic feasibility, e.g. 'watering with fire' fails Yogyata), and Asatti (proximity).",
            "difficulty": "medium",
            "question_type": "conceptual"
        }
    ]
    for q in s7_m6:
        q.update({"id": q_id, "subject": s_name, "subject_code": s_code, "module": s7_m6_name, "module_number": 6})
        questions.append(q)
        q_id += 1

    return questions, q_id

if __name__ == "__main__":
    qs6, id6 = generate_s6_questions(1)
    qs7, id7 = generate_s7_questions(id6)
    print(f"Generated {len(qs6)} questions for Subject 6 and {len(qs7)} for Subject 7. Total: {len(qs6)+len(qs7)}")
