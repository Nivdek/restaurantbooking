## RestaurantBooking

This site is still a work in progress and not a final product/release.

A test account is available for use with the credentials;

Username: `restaurantaccount`
Password: `restaurant123`

The aim of the website is to allow restaurant owners to create an account from which they can
then create and manage their restaurants and also take bookings for their restaurants.
Upon entering the website you arrive at the main page where all the restaurants that are available for booking
are displayed. This site view is the only one a visitor interested in making a reservation will need to access,
as the account section of the site is strictly for business accounts.

Important notes when using the test account:

While login / signup / logout pages do exist and work they are as of now unstyled and need to be accessed by appending the following to the base url;
1. /accounts/login/
2. /accounts/logout/
3. /accounts/signup/

Once logged in and redirected to the accountoverview page there are three navigatable tabs for the user;
1. Profile - Where the user can manage their account and update their contact info.
2. Bookings - Where booking requests for the restaurants owned by the account are displayed. These are split into two sections;
    - Active Bookings - These are the bookings which have been confirmed by the restaurant owner.
    - Booking Requests - These bookings are awaiting confirmation/rejection by the restaurant owner.
3. Restaurants - Where the currently available restaurants owned by the account are displayed.

------

### Intended Features

As the project in it's current state remains unfinished here will be outlined a list of changes or features to implemented.

**Booking Form:** The booking form for making a reservation will be updated with a better method for phone number collection. The Date/Time input will also be made to look better.
Along with this an automatic email confirmation will be sent to the supplied email address.

**Account Authentication:** The login/logout/signup account pages will be styled in line with the rest of the project, logout navigation will be made easily accessible on the account page.
                            The email verification function when creating an account will also be appropriately styled.

**Profile Page:** Most of the intended features for the profile page are in place, some additional styling is needed.

**Bookings Page:** The items in the two booking lists are currently clickable but do no lead anywhere.
The intention is that each booking, when clicked, will lead to a detailed view of the booking.
In this detailed booking view the owner can then approve/deny the request, read any additional notes, and more.

**Restaurants Page:** Here a list of the restaurants owned by the account will be displayed, just as the bookings page these objects are intended to be clickable.
The owner can then manage important information about the restaurant, such as the address, phone number or the about section.
The owner can also delete any unwanted restaurants with the click of a button.

**Contact Admin:** A feature for contacting the admin is planned for implementation.
This feature will take two forms;
- A report feature where any visitor easily can report a restaurant object for a list of reasons, eg. false advertising, incorrect address, or more.
- A contact feature for accounts where they can easily send a message to the admin regarding anything important. Such things could be; asking for status of a pending Restaurant posting,
help terminating an account, feature requests or more.


------

