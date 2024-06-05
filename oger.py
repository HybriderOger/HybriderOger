import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a new figure
fig, ax = plt.subplots(figsize=(6, 6))

# Body
body = patches.Ellipse((0.5, 0.3), 0.3, 0.4, color='lightgreen', ec='black')
ax.add_patch(body)

# Ears
left_ear = patches.Ellipse((0.3, 0.6), 0.1, 0.2, angle=30, color='lightgreen', ec='black')
right_ear = patches.Ellipse((0.7, 0.6), 0.1, 0.2, angle=-30, color='lightgreen', ec='black')
ax.add_patch(left_ear)
ax.add_patch(right_ear)

# Head
head = patches.Circle((0.5, 0.6), 0.2, color='lightgreen', ec='black')
ax.add_patch(head)

# Eyes
left_eye = patches.Circle((0.43, 0.65), 0.04, color='white', ec='black')
right_eye = patches.Circle((0.57, 0.65), 0.04, color='white', ec='black')
left_pupil = patches.Circle((0.43, 0.65), 0.02, color='black')
right_pupil = patches.Circle((0.57, 0.65), 0.02, color='black')
ax.add_patch(left_eye)
ax.add_patch(right_eye)
ax.add_patch(left_pupil)
ax.add_patch(right_pupil)

# Nose
nose = patches.Circle((0.5, 0.57), 0.03, color='green', ec='black')
ax.add_patch(nose)

# Mouth
mouth = patches.Arc((0.5, 0.5), 0.1, 0.05, angle=180, theta1=0, theta2=180, color='black')
ax.add_patch(mouth)

# Arms
left_arm = patches.Ellipse((0.3, 0.3), 0.1, 0.3, angle=30, color='lightgreen', ec='black')
right_arm = patches.Ellipse((0.7, 0.3), 0.1, 0.3, angle=-30, color='lightgreen', ec='black')
ax.add_patch(left_arm)
ax.add_patch(right_arm)

# Legs
left_leg = patches.Ellipse((0.4, 0.1), 0.1, 0.2, color='lightgreen', ec='black')
right_leg = patches.Ellipse((0.6, 0.1), 0.1, 0.2, color='lightgreen', ec='black')
ax.add_patch(left_leg)
ax.add_patch(right_leg)

# Hair
hair = patches.RegularPolygon((0.5, 0.8), 3, 0.05, color='darkgreen', ec='black')
ax.add_patch(hair)

# Set limits and hide axes
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Show the plot
plt.show()
