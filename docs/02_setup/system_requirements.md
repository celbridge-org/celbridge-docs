# System requirements { #doc-system-requirements }

This page contains system requirements for the Celbridge workbench application.
These specifications are given for informative purposes only, but they can be
referred to if you're looking to build or upgrade a system to run Celbridge on.

These are the **minimum** specifications required to run the Celbridge workbench application.

At present Celbridge is available fo Windows and macOS systems.


!!! note

    It is planned to create a Linux version of Celbridge in the future...


## Windows desktop or laptop PC - minimum requirements

| **CPU** | **Windows:** x86_32 CPU with SSE2 support, x86_64 CPU with SSE4.2 support, ARMv8 CPU<br>- *Example: Intel Core 2 Duo E8200, AMD FX-4100* |
|---|---|
| **RAM** | 4 GB |
| **Storage** | 200 MB (used for the executable, project files and cache).<br>Exporting projects requires downloading export templates separately<br>(1.3 GB after installation). |
| **Operating system** | Windows 10 |

## macOS desktop or MacBook - minimum requirements

| **CPU** | Apple silicon (M1 or later)<br>- *Intel Macs are not supported: the app ships as an Apple silicon build only, and Rosetta cannot run it* |
|---|---|
| **RAM** | 8 GB |
| **Storage** | the Celbridege application takes up around 350 MB
| **Operating system** | macOS 15 "Sequoia" or later |

!!! note

    Nothing else needs to be installed on a Mac. Celbridge bundles its own .NET runtime, and
    the document editors use the WebKit engine built into macOS. 
