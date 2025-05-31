import matplotlib.pyplot as plt
import numpy as np
import pytz
from datetime import datetime
from matplotlib.animation import FuncAnimation

def create_clock_circle():
    # Set up the figure and axis
    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    # Create a circle for the clock
    clock_face = plt.Circle((0, 0), 1, edgecolor='black', facecolor='white')
    ax.add_patch(clock_face)

    # Add hour markers
    for h in range(1, 13):
        angle = np.deg2rad((h / 12) * 360)  # Calculate the angle for each hour
        x = 0.8 * np.sin(angle)  # x position of the hour marker
        y = 0.8 * np.cos(angle)  # y position of the hour marker
        ax.text(x, y, str(h), ha='center', va='center', fontsize=12, weight='bold')

    # Add the center point of the clock
    ax.plot(0, 0, 'ko')

    # Set limits and remove axes
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.axis('off')

    # Initialize the hands
    hour_hand, = ax.plot([], [], lw=6, color='black')
    minute_hand, = ax.plot([], [], lw=4, color='black')
    second_hand, = ax.plot([], [], lw=2, color='red')

    # Function to update the hands
    def update(frame):
        # Set timezone to Asia/Phnom_Penh
        timezone = pytz.timezone("Asia/Phnom_Penh")
        current_time = datetime.now(timezone)

        # Extract the hour, minute, second, and period (AM/PM)
        hour = current_time.hour % 12  # Convert to 12-hour format
        minute = current_time.minute
        second = current_time.second
        period = "AM" if current_time.hour < 12 else "PM"

        # Calculate the angles for hour, minute, and second hands
        hour_angle = np.deg2rad(360 * (hour / 12) + (minute / 60) * 30)  # Hour hand
        minute_angle = np.deg2rad(360 * (minute / 60))  # Minute hand
        second_angle = np.deg2rad(360 * (second / 60))  # Second hand

        # Update the hand positions
        hour_hand.set_data([0, 0.5 * np.sin(hour_angle)], [0, 0.5 * np.cos(hour_angle)])
        minute_hand.set_data([0, 0.7 * np.sin(minute_angle)], [0, 0.7 * np.cos(minute_angle)])
        second_hand.set_data([0, 0.9 * np.sin(second_angle)], [0, 0.9 * np.cos(second_angle)])

        # Add AM/PM label at the top right of the clock
        ax.text(0.6, 1.0, period, ha='center', va='center', fontsize=15, weight='bold')

        return hour_hand, minute_hand, second_hand

    # Animate the clock
    ani = FuncAnimation(fig, update, interval=1000, blit=True, cache_frame_data=False)

    plt.show()

create_clock_circle()
