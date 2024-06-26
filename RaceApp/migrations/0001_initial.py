# Generated by Django 4.2.5 on 2024-02-21 17:06

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('displacement', models.CharField(max_length=50)),
                ('max_power', models.CharField(max_length=50)),
                ('max_torque', models.CharField(max_length=50)),
                ('additional_features', models.TextField()),
                ('rent_per_day', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='bike_images/')),
                ('available_count', models.PositiveIntegerField(default=0)),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booked_date', models.DateField(default=datetime.datetime.now)),
                ('is_completed', models.BooleanField(default=False)),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RaceApp.bike')),
            ],
        ),
        migrations.CreateModel(
            name='LapTimeEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rider_name', models.CharField(max_length=100)),
                ('lap_time', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='RacingRider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rider_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('license_pdf', models.FileField(upload_to='license_pdfs/')),
            ],
        ),
        migrations.CreateModel(
            name='StaffProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=10)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('aadhaar_card', models.ImageField(blank=True, null=True, upload_to='aadhaar_cards/')),
                ('joining_date', models.DateField(auto_now_add=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pictures/')),
            ],
        ),
        migrations.CreateModel(
            name='Trackday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.CharField(max_length=15)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DurationField(blank=True, null=True)),
                ('category', models.CharField(blank=True, max_length=20, null=True)),
                ('lap_time_entered_at', models.DateTimeField(auto_now_add=True)),
                ('total_race_time', models.CharField(default='00:00:00', max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TrackdayRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rider_name', models.CharField(max_length=255)),
                ('trackday_date', models.DateField()),
                ('number_of_trackdays', models.PositiveIntegerField(choices=[(1, '1'), (2, '2')], default=1)),
                ('gearrental', models.BooleanField(default=False)),
                ('vehiclerental', models.BooleanField(default=False)),
                ('licensepdf', models.FileField(blank=True, null=True, upload_to='licenses/')),
                ('profilepicture', models.ImageField(blank=True, null=True, upload_to='profile_pictures/')),
                ('rider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RiderDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('confirmation_date', models.DateField()),
                ('trackdays', models.PositiveIntegerField()),
                ('trackday_date', models.DateField()),
                ('current_status', models.CharField(max_length=10)),
                ('vehicle_name', models.CharField(max_length=100)),
                ('rental_amount_per_day', models.DecimalField(decimal_places=2, max_digits=10)),
                ('number_of_trackdays', models.PositiveIntegerField()),
                ('total_rental_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_trackday_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('vehicle_image', models.ImageField(blank=True, null=True, upload_to='vehicle_images/')),
                ('rider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rider_name', models.CharField(max_length=100)),
                ('trackday_date', models.DateField()),
                ('number_of_trackdays', models.IntegerField()),
                ('rental_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('confirmed_date', models.DateTimeField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='payment_record', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyTrackdayRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('trackday_date', models.DateField()),
                ('rider_details_pdf', models.FileField(upload_to='rider_details_pdfs/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyRaceTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('race_time', models.CharField(blank=True, max_length=10, null=True)),
                ('racer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RaceApp.racingrider')),
            ],
        ),
        migrations.CreateModel(
            name='Bookingconfirmed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmed_date', models.DateTimeField(auto_now_add=True)),
                ('trackday_date', models.DateField()),
                ('number_of_trackdays', models.PositiveIntegerField(choices=[(1, '1 day'), (2, '2 days')], default=1)),
                ('total_rental_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_trackday_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('upcoming', 'Upcoming'), ('in_progress', 'In Progress'), ('over', 'Over'), ('cancelled', 'Cancelled')], default='upcoming', max_length=15)),
                ('cancelled_date', models.DateTimeField(blank=True, null=True)),
                ('cancellation_status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=15)),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RaceApp.bike')),
                ('rider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BookingConfirmation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmation_date', models.DateField(default=datetime.datetime.now)),
                ('additional_details', models.TextField(blank=True, null=True)),
                ('total_rent', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Over', 'Over')], default='Active', max_length=10)),
                ('booking', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='RaceApp.booking')),
                ('trackday_registration', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='RaceApp.trackdayregistration')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='rider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='booking',
            name='trackdayregistration',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='RaceApp.trackdayregistration'),
        ),
        migrations.CreateModel(
            name='BikeRental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rented_at', models.DateTimeField(auto_now_add=True)),
                ('rider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
