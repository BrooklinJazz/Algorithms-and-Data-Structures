# Chapter 1
## Nuts and Bolts
- hosts and end systems
- communication links and packet switches
- physical media: coaxial cable, copper wire, optical fiber, radio spectrum
- packet switches: routers and link-layer switches
- route or path through the network
- ISPs: residential (local cable or telephone), corporate, university, airports, hotels, shops, cellular data isps
	- boardband access cable modem or DSL

## Protocols
- TCP (Transmission control protocol)
- IP Internet Protocol
- TCP/IP (principal protocols)
- internet standards (Internet Engineering Task FOrce (IETF))
- requests for comments (RFCs)
- HTTP
- IEEE 802 LAN/MAN Ethernet and wireless WiFi Standards

## A Services Description
an infrastructure that provides services to applications
"distrbuted applications" since they involve mutiple end systems that exchange data with each other
- run on end systems, not in the packet switches in the network core
- end sustems attached to the Internet provide an `socket interface
- protocol analogy as good manners

## Home Access
- DSL Digital Subscriber Line and cable
- obtained from the company that provides its wired local phone access
- (telco = telephone company)
- when DSL is used a customers telco is also it's ISP
- DSL uses the existing phone line (twisted pair copper wire)
- DSL exchanges data with the digital subscriber line access mutliplexer DLSAM located in the telco's local central office CO
- home DSL modem takes the digital data and translates it to high frequency tones for transmission over telephone wires. these "analog" signals are translated back into digital format at the DSLAM
- residential telephone line carries both data and traditional telephone signals simultaneously which are encoded at different frequencies
	- A high-spedd donwsteam channel: 50 kHz to 1 MHz band
	- a medium-speed upstream channel: 4kHz to 50kHz band
	- An ordinary two-way telephone channel: 0 to 4kHz band
- makes the single DSL link appear as if there were three separate links so that  a telephone call and an Internet connection can share the DSL link at the same time
- frequency division mutliplexing (technique above)
- DSL uses teclo's existing local telephone infrastructure

## Cable Internet Access
- cable internet access uses cable television company's existing cable televison infrastructure
- fiber and cable used for cable internet access: called hybrid fiber coax HFC 
- special cable modems connect to home PC through an enternet port
- CMTS cable modem termination system similar to DSLAM turning the analog signal sent from the cable modems in downstream back into digital format
- DOCSIS 2.0 standard defines downstream rates up to 42.8 Mbps and upstream rates of up to 30.7Mbps (asymetric access)
- shared broadcast medium (every packet sent by a home travels on the upstream channel to the head end. thus usage can affect other users rates
- a distributed multiple access protocol is needed to coordinate transmissions and avoid collisions.

## Fiber
- Fiber to the home FTTH
- provide an optical fiber path from the CO directly to the home.
- direct fiber: one fiber leaving the CO for each home

## Ethernet and WiFi
- LAN used to connect an end system to the edge router
- Ethernet use twisted-pair copper wire connect to an ethernet switch
- wireless LAN setting
- writeless transmit/receive packets to/from an access point
- end system (laptop) -> access point -> wired Internet
- must usually be withing a few tens of meters of the access point
- Wireless LAN access based on IEEE 802.11 tech (WiFi)

## Wide area wireless access: 3G and LTE
- same wireless infrastructure used for cellular telephony through a base station
- packet switches wide-area wireless Internet access up to 1 Mpbs
- 4G of wide-area wireless networks
- LTE: 10Mbps

## Physical Media
- life of a bit
	source end system -> first router -> second router -> ...n router -> 
- transmitter/receiver pairs
- bit is sent by progagating electromagnetic waves or optical pulses across a physical medium
- eg: twisted-pair copper wire, coaxial cable, multimode fiber-optic cable, terrestrial radio spectrum, satellite radio spectrum
- guided and unguided media
- guided: solid medium such as fiber optic cable
- propogate in the atmosphere and in outer space such as wireless LAN or satellite channel

## Twisted-Pair Copper Wire
- two insulated copper wires twisted together to reduce the electrical interference
- a number of pairs are bundled together by wrapping the pairs in a protective shield
- a pair constitutes a single connection link
- UTP is commonly used for computer networks for LANs 10Mbps - 10Gbps

## Coaxial Cable
- two copper conductors like twisted-pair
- concentric rather than parallel
- common in cable television systems
- coupled with cable modems to provide residential Internet access
- guided shared medium
- a number of end systems an be connected directly to the cable with each end system receiving whatever is sent by the others

## Fiber Optics
- thin flexible medium that conducts pulses of light with each puls representing a bit
- fast bit rates even hundreds of Gbps
- immune to electromagnetic interference
- low signal attenuation up to 100Km
- hard to tap
- prefered long-haul guided transmission media particularely for overseas links
- many long distance telephone networks in US now use fiber optics exclusively
- backbone of the Internet
- high cost of optical devices such as transmitters, receivers, and switches hidered deployment for short-haul transport
- OC Optical Carrier speeds range from 51.8Mbps to 39.8Gbps
	- OC-n where the link speed equals n oo 51.8 Mbps
	- include standards OC-1 and others

## Terrestrial Radio Channels
- electromagnetic spectrum
- no physical wire
- can penetrate walls
- long distances
- environment determins path loss and shadow fading decreasing signal strength as it moves around/through obstructing objects
- multipath fading due to reflection off interfering objects
- interference due to other transmissions and electromagnetic signals

## Satellite Radio Channels
- a communication satellite links two or more Earth-based microwave transmitter/receivers known as ground stations
- receives on one frequency band, regenerates the signal using a repeater, and transmits the signal on another frequency
- two used in communications: geostationary satellites and low-earth orbiting (LEO) satellites
- geostationary: remain in same spot on Earth
	- 36K Km above earth = substation signal propogation delay of 180 ms
	LEO satellites
 
## Packet Switching
- to send a message the source braks long messages into smaller chunks of data (packets)
- each packet travels through communication links and packet switches: (routers and link-layer switches)
- rate equal full transmission rate of the link: L bits over R rate then T time = L/R

# Store and Forward Transmission
- must recieve the entire packet before it can begin to transmit the first bit of the packet onto the outbound link
- each router adds 1L/R to the time it takes to send/receive packet to destination

## Queuing Delays and Packet Loss
- packet switch has an output buffer (AKA output queue) which stores packets that router is about to send into that link
- a full output buffer results in packet loss of either arriving packet or an already queued packet
- routing protocols: router examines the address and searches its forwarding table. using this destination adress to find the appropritate outbound link. The router then directs the packet to this outbound link.

- trace route program traceroute.org

## Circuit Switching
- the resources needed along a path (buffers, link transmission rate) to provide for communication between the end systems are reserved for the duration of the communication session. packet switched networks are not reserved. a sessions messages use the resources on demand and may have to queue for access. analogy to having a reservation vs waiting in line.
- telephone network is an example of circuit switching because a connection must first be established: called a circuit. guarantees a constant rate of transmission

## Multiplexing in Circuit Switched Networks
- FDM: frequency-division multiplexing
- TDM: time-division multiplexing
- FM stations use FDM to share the frequency spectrum between 88MHz and 108 MHz
- TDM link is divided into frams of a fixed duration and each fram is divided into a fixed number of time slots
- circuit switching is wasteful vs packet switching because dedicated circuits are idle during silent periods

## Packet Switching Vs Circuit Switching
- packet not suitable for realtime because of vartiable and unpredictable end to end delays
- packet switching offers better sharing of transmission capacity.
- packet switching simpler, more efficient, and less costly

## Network of Networks
- Tier 1 ISP -> Regional ISP -> Access ISP
- PoPs points of presence: a group of one or more routers at the same location where customer ISPs can connect into the provider ISP. can lease a high speed link
# Terms
- queuing delays
- output buffer
- geostationary satellites
- LEO satellites
- UTP: Unshielded twisted pair
- coaxial cable
- multimode fiber-optic cable
- terrestrial radio spectrum
- satellite radio spectrum
- electromagnetic waves
- optical pulses
- transmitter/receiver pairs
- LTE: Long Term Evolution
- packets
- Ethernet Switch
- twisted pair copper wire
- LAN: local area network
- FTTH
- DSL
- CO
- HFC
- CMTS
- DSLAM
- DOCSIS
- ISP
- IETF
- RFC
- TCP
- IP
- TCP/IP
- HTTP
- IEEE 802 LAN/MAN

# Questions
- what is a band?
- what is DSLAM?
- what is DLS?
- how the F do we transmit high frequency tones through DSL???
- what is frequency division multiplexing
- what are the 3 signals transmitted through a single DSL link? at what frequency?

