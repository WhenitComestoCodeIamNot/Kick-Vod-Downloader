import subprocess
import tkinter as tk
from tkinter import simpledialog, messagebox
import os
import re

# Function to check if a URL ends with .m3u8
def is_valid_m3u8_url(url):
  return url.lower().endswith(".m3u8")

# Function to extract year, month, and date from the URL
def extract_date_from_url(url):
  match = re.search(r"/(\d{4})/(\d{1,2})/(\d{1,2})/", url)
  if match:
    year, month, day = match.groups()
    # Ensure two-digit month and day format
    month = str(int(month)).zfill(2)
    day = str(int(day)).zfill(2)
    return year, month, day
  return None, None, None

while True:
  # Create a tkinter window
  root = tk.Tk()
  root.withdraw()  # Hide the main window

  # Create a popup dialog to enter the M3U8 URL
  m3u8_url = simpledialog.askstring("M3U8 URL", "Enter the M3U8 URL:")

  # Check if cancel button is pressed or invalid URL
  if m3u8_url is None or not is_valid_m3u8_url(m3u8_url):
    if m3u8_url is None:
      # Exit the script if cancel button is pressed
      break
    else:
      messagebox.showerror("Invalid URL", "The provided URL is not a valid .m3u8 link.")
      continue

  # Extract year, month, and date from the URL
  year, month, day = extract_date_from_url(m3u8_url)

  # Define the default text for -o based on the URL input
  default_output_text = "Mr Sins Travels"
  if year and month and day:
    # Use strftime to format the date with leading zeros if necessary
    date_string = f"{month:02}-{day:02}-{year}"
    default_output_text = f"{default_output_text} - {date_string} part1"

  # Get custom filename or use default
  while True:
    custom_output = simpledialog.askstring("Custom -o Parameter", f"Enter a custom -o parameter (default: {default_output_text}):", initialvalue=default_output_text)

    # Check if cancel button is pressed
    if custom_output is None:
      # Exit the script if cancel button is pressed
      break

    # Use the custom output parameter or the default if not provided
    output_parameter = custom_output if custom_output else default_output_text

    # Break loop if valid filename provided
    break

  # Define the target directory and full output path
  target_directory = "D:\\Videos\\Kick Vods\\MrSins"

  # Add a counter to handle duplicate names
  counter = 1
  output_file = os.path.join(target_directory, f"{output_parameter}.%(ext)s")
  while os.path.exists(output_file):
    counter += 1
    output_file = os.path.join(target_directory, f"{output_parameter} - part{counter}.%(ext)s")

  # Define the command with the desired parameters
  yt_dlp_command = [
    "d:\\Downloads\\YouTube Downloader\\August\\yt-dlp_win\\yt-dlp",
    "-v",
    "-P", target_directory,
    "-o", output_parameter + ".%(ext)s",
    m3u8_url
  ]

  # Run the yt-dlp command to download the video
  subprocess.run(yt_dlp_command)

  # Display a "Finished" popup when the download is complete
  messagebox.showinfo("Finished", "Download is complete.")

  # Break the loop after download finishes
  break
