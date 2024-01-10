# transport
A trip management software for a goods transport company. Contain two app namely app and agent.


functionality:
manage bookings and trips.
monitor trips state and progress.
summarize transporter's closed trips and calculate their wages.
manage trips report.


key-features:
users authentication and authorisation.
users management.
web-based barcode scanner. 
rea time trips update.
logging system.
customizable admin interface.
responsive interface across devices.



There will be 4 type of user.
1. agent - submit trips report (admin: no permission).
2. supervisor - manage trips (admin: view trips and bookings permission).
3. manager(superuser)- create and monitor trips (admin: superuser permission).
4. payroll - manage transporters wages (admin: no permission)


user stories

AGENT: submit trips report.
login into the application synctrip page.
scan trip barcode to sync trip.
submit reports for the synced trip.
view synced trip info.


SUPERVISOR: Manage trips.
login into the application manage page.
view all assigned trips.
manage trip progress.
manage trip reports.
monitor trips report status.
track trip location on map.


MANAGER: create trips.
login into the application admin interface.
in the booking model, add a new booking record.
in the trip model, create a new trip for the new booking.


MANAGER: monitor trips.
login into the application monitor page.
view all open trips.
monitor trips progress.
monitor trips latest report.
close trip


PAYROLL: manage transporters wages.
login into the application payroll page.
enter transporter id.
select a date to calculate their wages from.
click the process button.
view transporter trip summary and wages.

