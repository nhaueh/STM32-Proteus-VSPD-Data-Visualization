# 🛰️ STM32 Virtual HIL: UART Bridge to PC Plotter 📈

<p align="center">
  <img src="https://img.shields.io/badge/STM32-C8T6-03234B?style=for-the-badge&logo=stmicroelectronics&logoColor=white" />
  <img src="https://img.shields.io/badge/Proteus-8.15-005D91?style=for-the-badge&logo=proteus&logoColor=white" />
  <img src="https://img.shields.io/badge/VSPD-Virtual_COM-FFD700?style=for-the-badge&logo=data-bridge&logoColor=black" />
  <img src="https://img.shields.io/badge/PlatformIO-IDE-F5822A?style=for-the-badge&logo=platformio&logoColor=white" />
</p>

> **Hardware-in-the-Loop (HIL)** simulation project bridging embedded firmware with PC-side data visualization using Virtual Serial Ports.

---

### 🌟 Project Overview
This project demonstrates a complete integration workflow for embedded systems: from peripheral configuration and circuit simulation to establishing a virtual communication tunnel for real-time telemetry plotting.

---

### 🛠 Development Workflow (Step-by-Step)

#### **1️⃣ Peripheral Configuration ⚡ (STM32CubeMX)**
- Initialized the system clock and configured **GPIOs** for LCD control.
- Enabled **UART1** peripheral (115200-8-N-1) for high-speed data transmission.
- Generated the base project using the **Makefile** toolchain for seamless integration with VS Code.
![alt text]({748EA541-3F96-4D28-A030-7BDB6DD3E748}.png)
![alt text]({0C98F69D-2985-4027-81C5-26FF650EC748}.png)
![alt text]({A23F1A66-2EF0-4B32-BDF6-3D9DD7F2A6B6}.png)


#### **2️⃣ Schematic Design & Virtual Prototyping 🧩 (Proteus)**
- Constructed the hardware model featuring the **STM32F103C8T6** microcontroller.
- Integrated a **16x2 LCD (LM016L)** for local status display.
- Implemented the **COMPIM** module to act as the physical-to-virtual serial gateway.
![alt text]({79055A5B-F4FF-4A6A-910D-8A6EA2FFCE50}.png)


#### **3️⃣ Firmware Migration 🏗️ (VS Code & PlatformIO)**
- Migrated the CubeMX-generated source files into the **PlatformIO** environment.
- Mapped the `include/` and `src/` directories to ensure full compatibility with the STM32 HAL drivers.
- Optimized the build process for real-time simulation debugging.
![alt text](image.png)

#### **4️⃣ Virtual Communication Tunneling 🔗 (VSPD)**
- Utilized **Virtual Serial Port Driver (VSPD)** to create a dedicated null-modem bridge (e.g., **COM1 ↔ COM2**).
- Linked the Proteus COMPIM module to the virtual bridge, enabling wireless data tunneling within the OS.
![alt text]({14271C71-5EA3-41C2-962C-413C7C4D8CD5}.png)
![alt text]({70914AE6-27E7-4954-9738-A854DD190067}.png)

#### **5️⃣ Real-time Data Visualization 📊 (Serial Plotter)**
- Connected the VS Code **Serial Plotter** to the receiving end of the virtual bridge (**COM2**).
- Successfully visualized real-time UART telemetry streams into dynamic graphical plots.
![alt text]({E29D9A3B-33A9-44C8-AA44-3DB44B16B38A}.png)
![alt text]({3862281E-22DD-4964-B6D2-A98BEC2363BE}.png)
Preview:
![alt text]({9EA088F1-D328-4BEE-B962-4F1FE295268B}.png)
![alt text]({8EFD162E-5C09-46EF-9049-F5636E1824AD}.png)
---