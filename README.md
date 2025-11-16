# Booking Manager App

## Description

This is a simple booking management application built using Python and Tkinter. It allows users to manage reservations for multiple rooms, as well as enabling/disabling notifications for successful bookings. The app supports basic features like selecting rooms, making bookings, and receiving notifications when a booking is successful.

## Prerequisites

- **Python** (version 3.x recommended)
- **Tkinter** (for GUI components)
- **Plyer** (for notifications)

To install Plyer, use the following pip command:

```bash
pip install plyer
```

## How to Run

1. Clone or download the repository to your local machine.

2. Open a terminal and navigate to the project folder.

3. Run the script with:

   ```bash
   python main.py
   ```

4. Follow the prompts in the terminal or interact with the GUI to book rooms or adjust settings.

## Features

1. **Room Booking:**

   - Choose from different rooms and select a booking time.
   - Confirm the booking and receive success messages.
   - Optionally, enable notifications for successful bookings.

2. **Settings:**

   - Enable or disable notifications for successful bookings.
   - Change other app settings in the future as required.

3. **Room Availability:**

   - View if rooms are available or already occupied.
   - Display detailed room information such as capacity and availability.

## How to Use

1. **Start the application**:
   Upon starting the app, you’ll be greeted with a welcome screen with two options:

   - **1**: Make a reservation
   - **2**: Access settings

2. **Booking a room**:

   - Choose from one of the available rooms (Sala 1, Sala 2, Sala 3, Sala 4).
   - Input the required details, such as your name, and booking start and end time.
   - A confirmation message will appear, and if notifications are enabled, a notification will be sent to your desktop.

3. **Settings**:

   - You can toggle notifications on or off from the settings screen.

4. **Exit**:
   To exit the app, click the close button in the top-left corner of the window.

## User Interface

The user interface is simple and not heavily focused on design, as the app is more functionally oriented. Future improvements are planned for better aesthetics, but for now, the app uses a basic color scheme:

- Background: `#f7f7f7`
- Primary Text: `#333`
- Secondary Text: `#555`
- Button Background: `#808080`
- Hover Effect: `#778899`

## Code Overview

### Main Functions

- **Booking Workflow**:

  - Users can navigate through the app to select rooms and make bookings.
  - The system updates a JSON file (`sale.json`) with the booking details and marks rooms as occupied.
  - Notification support is built in, using **Plyer** to notify the user about successful bookings.

- **Settings**:

  - The settings screen allows users to toggle notifications on or off. The setting is stored in a file (`notifiche.txt`) to persist across sessions.

### Files:

- `sale.json`: Contains room data (room names, capacity, availability).
- `notifiche.txt`: Stores the status of notifications (enabled or disabled).

### Example Usage

Here is an example of how you might interact with the app:

1. Start the application.
2. Choose "Prenota Sala" (Book a Room).
3. Select a room (e.g., Sala 1).
4. Enter your name, booking start time, and end time.
5. Confirm the booking.
6. Receive a success message and a notification (if enabled).

## Known Issues

- The application assumes the file `sale.json` exists with the correct room data. If the file is missing or corrupted, it may not work as expected.
- Notifications depend on the availability of **Plyer** and may require certain platform-specific configurations.

## Future Improvements

- Improve the UI design for a more polished experience.
- Add support for multi-language interfaces.
- Implement a more sophisticated database for room availability.
- Introduce additional customization options in the settings.

---

**Author**: Christian Lancini
**Development Start Date**: November 9, 2025
**Version**: 1.0 (November 16, 2025)

---
