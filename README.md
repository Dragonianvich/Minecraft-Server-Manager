# Minecraft-Server-Manager

This project is a desktop application that helps players set up and manage a local dedicated Minecraft server with ease.

It automates and simplifies the server setup process by removing the need to manually:

. Download and organize server files
. Edit configuration files
. Manage basic server startup settings

The goal is to reduce the complexity of hosting a Minecraft server so users can get a working server running in minutes instead of dealing with manual setup steps.



What's new:

. Auto-detects if Java is installed and shows a clear error with a download link if it isn't
. Checks for server.jar before starting and tells you exactly where to place it if missing
. Automatically creates and accepts eula.txt so you don't have to manually edit it
. RAM allocation now shows the current GB value next to the slider
. Start and Stop buttons now disable/enable based on server state
. Server process is now safely terminated if it doesn't stop within 15 seconds
. Auto-update checker — the app will notify you on launch when a new version is available
. Dark Minecraft-themed UI with green accents

Requirements:

. Java 17 or newer — https://adoptium.net
. Download server.jar from https://minecraft.net/download/server and place it in the Minecraft Server Manager folder
. Port 25565 open in your router settings for others to join


How to Run:

1. go to releases and navigate to latest release
2. download and run the .exe

