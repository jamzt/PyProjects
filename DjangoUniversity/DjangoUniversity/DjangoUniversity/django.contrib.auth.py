from django.contrib.auth.models import User

# Replace 'your_username' with the actual username of the superuser
user = User.objects.get(username='jamz')

# Set a new password
user.set_password('Atake_1')

# Save the changes
user.save()

exit()