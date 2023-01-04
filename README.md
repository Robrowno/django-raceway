# Django Raceway 

Django Raceway is a fictional motor-circuit in the UK with an extensive pedigree in racing and caters to those who love high-speed thrills and the smell of petrol and burnt rubber first thing in the morning!

Django Raceway, as a B2C business, aims to deliver personalised trackdays to motorsports enthusiasts at a state-of-the-art track with many challenging configurations. Users can register for an account, book track days, hire cars and book tuition to improve their car control and lap times. They can also request bespoke trackdays on behalf of a company or group, contact the business directly or sign up to a motorsports newsletter.

This is the right place for you if you are:
    - Looking to take your own car on a highly technical track
    - Looking to try out different driving experiences to command different kinds of sports cars
    - Looking to hire a car or reserve a bespoke track day for an event or group.

This is my fifth and final portfolio project for my Diploma in Software Development through Code Institute, where I am specialising in E-Commerce applications. 


Responsiveness Image Here: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Link to live site: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

---

## Table of Contents:



---

## Wireframes and Planning


---

## User Experience (UX)


---

## Features


---

## Future Implementations

---

## Technologies Used

---

## Testing

---

## Bugs and Issues

- AWS Config: I was unable to deploy on Heroku thanks to a missing Variable in my User Groups that was spotted by Alan from Tutor Support. 

- I tried to use a for loop for my admin.py file to automate and speed up model registration. Whilst it sounded like a good idea in principal, it prevented me from adding list_display field options once they had been registered. I unregistered and re-registered the models to be able to do this.

- I had some early trouble getting my contact model to work correctly - I realised I had put incorrect 'name' attributes in my contact view. I also made changes in my contact model that required me to flush the database and remove previous migrations and to migrate again after.

- Bootstrap 5 toasts: I attempted to modify the bootstrap 4 toasts from the Boutique Ado walkthrough, whilst I was using Bootstrap 5.0.2 - This didn't work, and thanks to a snippet of code from Alan from Tutor support I was able to get it working again.



---

## Deployment

---

## Peer Reviews

---

## Credits

### Code Help:

The preliminary set up and an assisting walkthrough came in the form of following Code Institute's Boutique Ado walkthrough e-commerce project. Repository can be found here: [Boutique Ado - Code Institute](https://github.com/Code-Institute-Solutions/boutique_ado_v1)

I used the Bootstrap v5.0.2 framework to handle a lot of the heavy lifting of site styling and layout. 
The following from the documentation helped me:
- Navigation:
    - [Bootstrap 5 Navbar docs](https://getbootstrap.com/docs/5.0/components/navbar/)
    - [MD Bootstrap Navbar docs](https://mdbootstrap.com/docs/standard/navigation/navbar/#subsection-icons)
- Carousel:
    - [Bootstrap Carousel docs](https://getbootstrap.com/docs/5.0/components/carousel/)
- Cards: 
    - [Bootstrap Cards](https://getbootstrap.com/docs/5.0/components/card/)


For general Bootstrap tips and information, I frequently referred to the [GetBootstrap](https://getbootstrap.com/) documentation, the [mdbootstrap](https://mdbootstrap.com/docs/) documentation and the [W3Schools](https://www.w3schools.com/bootstrap5/index.php) bootstrap documentation.

Favicons were generated on [Favicon.io](https://favicon.io/favicon-converter/) - I converted one of the checkered flag images I have (see images below) into a favicon using their site.

I made use of Icons from [Font Awesome](https://fontawesome.com/) using their free student plan. 
All icons used in this project have come from here.

Validator code for preventing previous dates from being set for creating trackdays found on stackoverflow: [Prevent past dates being set](https://stackoverflow.com/questions/4941974/django-how-to-set-datefield-to-only-accept-today-future-dates)

I found the code for storing phone numbers in my models from stackoverflow as well: [Phone Number Validator](https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-a-phone-number-in-django-models)

I made a mock up of my checkout page using the template provided by [mdboostrap](https://mdbootstrap.com/docs/standard/extended/credit-card/) - With this I was better able to visualise what I needed in my checkout page and how I wanted it to look.


## Personal Credits

- Many Thanks to my C.I Mentor Daisy McGirr, who has been guiding me and advising me through this project as well as all projects since PP2 - Her input in our mentor sessions has been instrumental in getting me this far and so I have to say I massive thank you to her for that!

- Thanks to Monika Hrda, for support with helping with the idea for a constraint on my trackday model and reminding me about the debug var in my settings.py file. A massive thanks to her for her support and chats on my project. I'm looking forward to working on some projects with Monika in future!

- Ben Dawson, for taking calls with me to discuss our P5 ideas at the project inception stage, and hosting check-in calls with me to see how we were getting on at different stages in our projects.

- Alan from C.I tutor support - helped me work out an issue with my AWS configuration where I was stuck and sat in front of my screen for over 3 hours! He is so patient, understanding and methodical and has also helped me to debug an issue I was having with my bootstrap 5 toasts. Thanks Alan! 

- Ed from Tutor Support - Also a member of the London C.I group, he helped me when I wasn't able to extract string values from my model choices. He introducted me to the get_FOO_display() method from the Django Docs, which did exactly what I was looking for. Thanks Ed!


### Media/Images:
- Checkered Flags from Clipartmax: [Flag1](https://www.clipartmax.com/middle/m2H7d3N4d3i8d3i8_checkered-flag-icon-clipart-auto-racing-racing-flags-finish-flag-icon-png/), [Flag2](https://www.clipartmax.com/middle/m2i8G6Z5H7d3A0G6_finish-flag-race-racing-win-winner-finish-checkered-flag-icon-png/)

- Photographs in the Gallery:
    - [Porsche Trackday pic](https://www.porscheclubgb.com/news-and-events/news/2021/december/2022-porsche-club-gb-trackday-calendar-announced)
    - [Caterhams Trackday pic](https://reis.co.uk/what-are-the-most-popular-track-day-cars/)
    - [Track car pic](https://www.carmagazine.co.uk/best/track-day-car/)
    - [Ariel Atom pic](https://www.carmagazine.co.uk/best/track-day-car/)
    - [McLaren pic](https://www.carmagazine.co.uk/best/track-day-car/)
    - [Ferrari pic](https://www.topgear.com/car-news/motorsport/ferrari-might-have-invented-best-sounding-trackday-ever)
    - All Mini Pictures taken were given to me with permission from the photographer.

- About section images:
    - [Trophy Cabinet Image](https://www.cgeniae.ml/products.aspx?cname=trophy+cabinets+and+showcases&cid=102&xi=1&xc=19&pr=16.99)
    - [Formula Ford Image](https://www.autosport.com/national/news/formula-ford-festival-at-50-a-golden-era-as-the-ultimate-proving-ground/6714288/)
- Car hire images:
    - [Ariel Atom 3](https://www.therealgranturismo.com/online-store/ARIEL-ATOM-Trackday-Hire-p84763897)
    - [Porsche 996 GT3](https://www.elferspot.com/en/magazin/five-good-reasons-for-a-porsche-996-gt3/)
    - [Renault Megane RS](https://www.topgear.com/car-news/hot-hatch/these-are-12-best-hot-hatches-all-time)
    - [Radical Rapture](https://www.topgear.com/car-news/motorsport/new-radical-sr10-425bhp-turbocharged-track-toy)
    - [Lotus Image](https://www.evo.co.uk/lotus/exige/6226/lotus-exige-s2-buying-guide)
    - [Nissan GTR Image](https://www.carmagazine.co.uk/car-reviews/nissan/nissan-gt-r-track-edition-engineered-by-nismo-2016-review/)
- Experiences page images:
    - [Junior Experience image](https://www.roadandtrack.com/news/a35090134/toyota-gr-yaris-vs-civic-type-r-gti-fiesta-st/)
    - [Single Seater picture](https://driftlimits.co.uk/experience/f1000-thrill-experience/)
    - [Sportscar Experience image](https://thruxtonracing.co.uk/experiences/supercar-trio)
    - [Full Experience image](https://thruxtonracing.co.uk/experiences/supercar-trio)
- Tuition page:
    - [Bronze Image](http://clipart-library.com/clipart/1937119.htm)
    - [Silver Image](https://gallery.yopriceville.com/Free-Clipart-Pictures/Trophy-and-Medals-PNG/Silver_Trophy_Cup_Award_Transparent_PNG_Clip_Art_Image)
    - [Gold Image](https://gallery.yopriceville.com/Free-Clipart-Pictures/Trophy-and-Medals-PNG/Gold_Trophy_Cup_Award_Transparent_PNG_Clip_Art_Image#.Y5tTBuzP3Uo)
    - [Racing Driver Image](https://blog.demon-tweeks.com/motorsport/how-to-choose-a-race-suit/)


---
## Final Thoughts

---
