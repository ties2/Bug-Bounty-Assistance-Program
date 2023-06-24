1.1: definition

Organization includes:

•	digital data 
•	people
•	operation

people and operation are out of scope of vulnerabilities assessment or Penetration testing, so red tram does this task and make it full this gap

the task of red team is similarity of attacks in extended scope that include people and operations

Red team should simulate TTP (tactics, technique, procedures)

tactics like recon, persist, …

technique is use to accessing the tactics

the best groups for red team are APT

the APT group create new tactics and technique during their attacking and it’s not easy 

the red teamer should know:

•	Computer architecture (read book about this)
•	network
•	programming (c++, python)
•	Thinking outside the box


the aim of red team is review of operation of monitoring and security devices and check if there are no misconfiguration of EDR, XDR, SIEM,





•	Adversary emulation

normal red team is different from adversary emulation and in this scope, you just attack on special products of organization.

after about two years becoming red team, we can do adversary emulation and we should first know all current technique

the person who does adversary emulation has to expert on API call

•	Event Tracing for Windows (ETW)

https://learn.microsoft.com/en-us/windows-hardware/drivers/devtest/event-tracing-for-windows--etw-

https://www.ired.team/miscellaneous-reversing-forensics/windows-kernel-internals/etw-event-tracing-for-windows-101


Event Tracing for Windows (ETW) is a powerful tracing infrastructure built into the Windows operating system. It enables developers and system administrators to capture detailed diagnostic and performance information from various sources, including the kernel, drivers, and applications.
ETW works by instrumenting software components with providers that emit events, which are then captured by trace sessions. You can create and manage trace sessions using the Event Viewer tool, the logman command-line utility, or the Windows Performance Recorder.
To use ETW, you need to have administrative privileges on the Windows computer. Once you have access, you can use ETW to:
•	Monitor system and application performance
•	Diagnose issues related to software and hardware components
•	Debug software applications and drivers
•	Analyze and optimize system performance
Some examples of ETW providers that you can use to capture diagnostic and performance information include:
•	Microsoft-Windows-Kernel-Process
•	Microsoft-Windows-NetworkProfile
•	Microsoft-Windows-PowerShell
•	Microsoft-Windows-WinINet
•	Microsoft-Windows-WMI-Activity
To get started with ETW, you can use the Event Viewer tool to create a custom view that filters events based on specific criteria. You can also use the logman command-line utility to start and stop trace sessions, and to configure providers and filters.
Keep in mind that ETW generates a large amount of data, so it's important to use it judiciously and to analyze the results carefully to avoid overwhelming your system.


we can use this feature to detect API CALL of a exe file

when you anbale this tool you can have logs of API call of windows 
EDR check output of this tool

Note: it can have a heavy log


frequency of red team is intelligence-led (new exploit, tool, TTP)

frequency of Adversary emulation is 2 times every year

Red team:

•	software operation 
•	hardware operation

Doing red team operation:

first, we start with software operation

software operation:
•	Bas (use auto tools such as cobalt strike)
•	make tools ourselves (need knowledge about TTP, python ,WAC,C++)

Note: if we use malleable and change agent in cobalt and make custom profile it bypasses antivirus


Example-1:
•	virtualAlloc
•	RtlMovememory
•	createthread
•	waitForSinfleobject

Example-2:
•	HeapAlloc
•	HeapCreate
•	createThread
•	WaitForSinfloeobject


we use tools that do automation operation such as cobalt strike we call this technique BAS

note: we can write API windows with python and it has library for this  but when wants convert it , the file has big size it just make it high speed in some situation

•	WAC(windows API call)

there are a lot of windows API and we should learn them and also their alternative 

example: process injection use alternative and when use it EDR detect it.EDR check some important windows API and know the patern

we can put our payload on heap instead of stack and EDR doesn’t check heap

with this gathering this information we can do software operation 

3.1	Hardware operation 

in hardware filed red teamer should have one of the mini hardware such as 
 Raspberry

https://www.raspberrypi.com/products/

we should all kind of IOT in organization



minicomputer: raspberry pi zero, RockPro64, HummingBoard Pro, Cobex-12ex, NanoPi Neo2, Pycom fipy

RF: SDR, RTL-SDR v3, GPS bandpass filter, nRF52840 USB Dongle

HID: rubberducky, rduino, USBNinja, xploit Nano

Network: NAC Bypass, pwnplug r4

Note: we can use raspberry pi for nak bypass for example 

Book: The Hacker’s Hardware Toolkit


Note: nrf52840 dongle uses for detect IOT device and in radio frequency we need these tools

Note: zigbee is an IEEE 802.15.4-based specification for a suite of high-level communication protocols used to create personal area networks with small, low-power digital radios

in hid attack field we should use EXPLoit nano device

site: EXPLIOT

Note: this device use com instead of USB during connection and this device has another device beside that call DIVA and it use for testing like DWVA in pentesting 
some attack to device like parking door is simulate in this device

Note: HID


note: use pwn plug r3 device or r4 for network test

site: PacketFence

when use these device and modem LTE the data exit from another network and it can’t detect on SIEM
PWNIE express make hack hardware 

when organization use port security it becomes hard to do hardware operation (hack)


1.2	Methodology and framework 

there are some famous methodologies for red team like

•	MITRE ATT&CK
•	Cyber kill chain
•	CBEST
•	TIBER-EU

one of good EDRs is carbo because it has more predefine rule
kasper EDR has 10 rules but this is has 30 rules

Note: EDR like carbon and wazuh



•	BAS (bridge attack simulation)

tools and framework for doing red team

such as:

•	cobalt strike (with license)
•	caldera (open source)
•	infectionmonkey
•	Foreseeti
•	cymulate
•	attackiq
•	efendify


1.3 MITRE Att&Ck

https://www.google.com/search?client=safari&rls=en&q=mitre+att%26ck&ie=UTF-8&oe=UTF-8

•	Reconnaissance
•	Resource Development
•	Initial Acess
•	Execution
•	Persistence
•	Privilege Escalation
•	Defense Evasion
•	Credential Access 
•	Discovery
•	Lateral Movement
•	Collection
•	Command and Control
•	Exfiltration
•	Impact



CVE.mittre.org (technique)
CWE.mittre.org (main category of attack-tactics) https://cwe.mitre.org)


note: one of important attacks is UAF (use after free) it means a program has a lot of reference and when the program become close its reference stayed open and we use this feature
most of the Linux distribution are vulnerable to this attack.

note: processhearpaderping connect mimikatz process to chrome so it give Microsoft sign 


 MITRE has 14 tactics and every tactic has technique and technique has sub technique

site that we should sign up:

•	shodan (https://www.shodan.io/)
•	exploit.in (https://exploit.in)
•	zerodaylab (https://www.zdlgroup.com)
•	dark matter


MITRE defines a subdomain call Defend (d3fend.mitre.org)

note: klist (check it)

•	Microsoft Exploit protection


https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/enable-exploit-protection?view=o365-worldwide

