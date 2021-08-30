#!/bin/bash

# install dependencies
sudo pacman -Sy --noconfirm
sudo pacman -S --noconfirm --needed wine-staging winetricks
sudo pacman -S --noconfirm --needed giflib lib32-giflib libpng lib32-libpng libldap lib32-libldap gnutls lib32-gnutls mpg123 lib32-mpg123 openal lib32-openal v4l-utils lib32-v4l-utils libpulse lib32-libpulse alsa-plugins lib32-alsa-plugins alsa-lib lib32-alsa-lib libjpeg-turbo lib32-libjpeg-turbo libxcomposite lib32-libxcomposite libxinerama lib32-libxinerama ncurses lib32-ncurses opencl-icd-loader lib32-opencl-icd-loader libxslt lib32-libxslt libva lib32-libva gtk3 lib32-gtk3 gst-plugins-base-libs lib32-gst-plugins-base-libs vulkan-icd-loader lib32-vulkan-icd-loader cups samba dosbox
sudo pacman -S --noconfirm --needed lib32-mesa vulkan-radeon lib32-vulkan-radeon vulkan-icd-loader lib32-vulkan-icd-loader

# install proton-ge-custom
wget https://github.com/GloriousEggroll/proton-ge-custom/releases/download/6.16-GE-1/Proton-6.16-GE-1.tar.gz -O /tmp/Proton-6.16-GE-1.tar.gz
mkdir -p ~/.steam/root/compatibilitytools.d
tar -xf /tmp/Proton-6.16-GE-1.tar.gz -C ~/.steam/root/compatibilitytools.d/

# Restart Steam.
# Enable proton-ge-custom.
