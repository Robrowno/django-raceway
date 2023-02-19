# Manual and Automated Testing

This section of the documentation comprises of various manual and automated tests and online validators to check the quality of my code and also to check the functionality of the project.

See User Story:
[USER STORY: Testing]([#34](https://github.com/Robrowno/django-raceway/issues/34))

## Table of Contents

- [Manual Testing](#manual-testing)
- [HTML Validation](#html-validation)
- [CSS Validation](#css-validation)
- [JS Validation](#js-validation)
- [Python Validation](#python-validation)
- [Lighthouse Performance](#lighthouse-performance-testing)
- [Devices/Browsers](#device-and-browser-testing)
- [Known/Unresolved Bugs](#current-known-and-unresolved-issues)


---

## Automated Testing

Due to time constraints, I was under pressure to conclude the project and as a result I did not manage to get around to doing a thorough unittest of all the python urls, views, etc. 

I have managed to do some url resolutions, including some in the cars app, the checkout app and the profiles app.
Of the tests I have run, all pass. 

I will attempt to conduct a more thorough unittest of the project in future.


---

## Manual Testing

### Home/Index/Middle-Navigation
| Test | Method | Expected Outcome | Result |
| - | - | - | - |
| Django Raceway Logo/Home Link | Click on Logo at top of Page | Redirect to the home page | PASS |
| Carousel | Click on chevrons either side of carousel | Moves to next image slide in correct direction | PASS |
| Booking Link | Click on middle nav link | Opens Trackday Booking Page | PASS |
| Cars for Hire Link | Click on middle nav link  | Opens Car Hire Page | PASS |
| Tuition Link | Click on middle nav link  | Opens Tuition Page | PASS |
| Experiences Link | Click on middle nav link  | Opens Experiences Page | PASS |
| Contact Link | Click on middle nav link  | Opens Contact Page | PASS |
| About Page Link | Click on middle nav link  | Opens About Page | PASS |
| Gallery Modal Click | Click on a modal image in the Gallery | Expands image when clicked | PASS |
| Gallery Modal Next | Click on chevrons either side of the image | Moves to next image slide in correct direction | PASS |
| Gallery Modal Close | Click on the 'x' at the top of the image | Closes image model | PASS |


### Footer/Mailchimp
| Test | Method | Expected Outcome | Result |
| - | - | - | - |
| Policies Link | Click on link | opens the Policies page | PASS |
| FAQs Link | Click on link | opens FAQs Page | Pass |
| Up-Arrow button | Click on up-arrow button | Takes you to the top of the page | PASS |
| Sign Up Button in Footer | Click on Sign up button | Redirect to the Newletter sign up form/page | Pass |
| Subscribe/Mailchimp Newsletter | Enter a valid email and click on subscribe | Green confirmation text confirming subscription will appear | PASS |


### Trackday Booking Page/Booking Detail
| Test | Method | Expected Outcome | Result |
| - | - | - | - |
| Trackday Display | check Trackdays are rendering on the page by clicking on the 'booking' tab in the middle nav | Expect to see a list of upcoming trackdays, with details including base price displayed | PASS |
| Hide Trackday in Basket | add trackday to basket and return to trackday list page | trackday currently in the basket is hidden from user | PASS |
| Button change when Trackday in basket | add trackday to basket and return to trackday list page | buttons should change to reflect the face that you can only book one trackday at a time | PASS |
| Request Trackday Button | click on button | directs you to the track day request page and form | PASS |
| Availability counter update | checkout out with a trackday order succesfully and return to the trackday list | Availability of specific trackday will decrease | PASS |
| Booking Button change when full | Test what happens when a trackday's availability goes to 0 |  |  |
|  |  |  |  |


### Tuition/Experiences and Detail Pages
| Test | Method | Expected Outcome | Result |
| - | - | - | - |
| Tuition Page | Click on tuition tab | Opens tuition page where you will see list of tuition packages displayed | PASS |
| Experience Page | Click on experiences tab and | Opens experiences page where you will see list of experiences displayed | PASS |
| Tuition Detail | Open detail page through clicking explore button | Specific tuition package is opened with details and an itinerary on display | PASS |
| Experience Detail | Open detail page through clicking explore button | Specific experience package is opened with details and an itinerary on display | PASS |
| Quantity adjustments | Click on plus and minus buttons | quantity will increment/decrement and be reflected to the user. Will also cap at a max and min value | PASS |
| Booking button | Click on the book button | Item will be added to the basket with the correct quantity selected by the user | PASS |
|  |  |  |  |


### Trackday Request
| Test | Method | Expected Outcome | Result |
| - | - | - | - |
| Submit Button | Submit form without filling out any required fields | Form validation will prevent it from sending and alert the site user | PASS |
| Submit Button | Submit with one required input filled in only | Form validation will prevent it from sending and alert the site user | PASS |
| Email input | Try to enter an invalid email address or random numbers, words etc.  | Form will not send and user will be informed to enter a valid email address | PASS |
| Date input | Try to enter a past date or today's date | JS Alert will inform the user to enter a date no sooner than today | PASS |
| Number of spaces | Try to enter an incorrect number outside of the specified min and max | Form validation will prevent it from sending and alert the site user | PASS |
| Submit Complete Form | Submit a valid form via the submit button | Return to home page and inform user of successful submission with a success toast | PASS |
| Database | Check output of submission in the database | All filled out information should be strored correctly in the database | PASS |



### Contact
| Test | Method | Expected Outcome | Result |
| - | - | - | - |
| Submit Form | Attempt to submit blank form with nothing filled in | Form validation will prevent form from sending and alert user to which input needs filling in | PASS |
| Submit Form | Attempt to submit with just one input filled in  | Form validation will prevent form from sending and alert user to which input needs filling in | PASS |
| Email input | Try to enter an invalid email address or random numbers, words etc.  | Form will not send and user will be informed to enter a valid email address | PASS |
| Submit Valid Form | Submit a complete and valid contact form | Page redirects to a success version of the same page, informs the user it sent successfully | PASS |
| Return Home Button | Click on button | Redirects back to the Home page | PASS |
| Database | Check output of submission in the database | All filled out information should be strored correctly in the database | PASS |



### Profile
| Test | Method | Expected Outcome | Result |
| - | - | - | - |
| Profile Link | Check appearance when logged out | Profile page is not accessible to users not logged in | PASS |
| Profile Link | Check appearance and click on link when logged in | User will be redirected to their profile page | PASS |
| Edit Button | Click Edit Button | Form fields will become editable and the button will change to 'Save' | PASS |
| Save Button | Click Save Button | Form will save new details for user | Pass |
| Input fields | Enter invalid inputs for fields | User will get an error message | Pass |
| Input fields | Enter Valid input for fields | User will be informed that it saved successfully | PASS |



### Authentication
| Test | Method | Expected Outcome | Result |
| - | - | - | - |
| Sign Up | Create an account | You will be asked to verify your account and sent an email to verify it | PASS |
| Verification Email | Click on email link to verify account | Upon click, you will be redirected to the site where it will be confirmed that your account is verified | PASS |
| Login | Login with a registered account | Redirected to homepage and informed you are logged in | PASS |
| Remember me checkbox | Click on remember me checkbox button before loggin in | You will not need to login next time you visit the site | PASS |
| Forgot Password | Click on Forget Password and submit email | Link to set new password sent to email address supplied by user | PASS |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

### Basket and Checkout
| Test | Method | Expected Outcome | Result |
| - | - | - | - |
| Basket Link | Click on Basket link in top nav | Redirects to basket page | PASS |
| Checkout Link | Have nothing in the basket and check basket icon for visibility  | If nothing is in the basket, the checkout page will be hidden | Pass |
| Basket Page with no items | Click on basket page with nothing in the basket | Item counter reads as 0 and user is informed that there are no items in the basket, summary is blank | PASS |
| Item in Basket | Add item to basket and check that it appears in the items table | Chosen product will appear in the basket | PASS |
| Multiple items in Basket | Add more than one item to the basket (both quantity and different products) | Quantities are implemented and counted and you are able to add all 3 different products to basket in any order | PASS |
| Delete Item in basket | Click 'Delete button | Item is deleted from the basket | PASS |
| Summary total Calculator | Add items to basket, change quantities, delete items from basket | total will adjust accordingly | PASS |
| Summary VAT calculator | Add items to basket and check VAT calculation | 20% VAT applied automatically | PASS |
| Checkout Button (Basket Page) |  |  |  |
| Checkout Button (Nav Link) |  |  |  |
| Checkout  |  |  |  |
| Checkout Success |  |  |  |
| Checkout Cancel |  |  |  |
| Checkout Fail |  |  |  |
| Confirmation Email |  |  |  |
| Order History Added/Updated |  |  |  |

### Management
| Test | Method | Expected Outcome | Result |
| - | - | - | - |
| Management Link | Login as Admin/Superuser and open profile dropdown | Management link visible and when clicked, redirect to the management add trackday page | PASS |
| Submit Form |  |  |  |
| Image upload to AWS |  |  |  |
| Superuser Access only |  |  |  |
| Trackday list |  |  |  |
| Form validation |  |  |  |
|  |  |  |  |


### Other
| Test | Method | Expected Outcome | Result |
| - | - | - | - |
| Order History Link | click on link in Nav | Opens user order history page | PASS |
| Order History Table | Make orders and view order history page | Orders will render in a table automatically and in chronological order | PASS |
| Stripe Receipt Link | Click receipt link in the table | Redirects to Stripe receipt | PASS |


---

## HTML Validation

All HTML validation was done using https://validator.w3.org/nu/


### /templates 

| File | Result |
| -------- | ------ |
| base.html | PASS |
| main-nav.html  | PASS |
| includes/base.html | PASS |
| includes/toast_error.html  | PASS |
| includes/toast_info.html  | PASS |
| includes/toast_success.html  | PASS |
| includes/toast_warning.html | PASS |

### /trackdays

| File | Result |
| -------- | ------ |
|  experience-detail.html | PASS |
|  experiences.html | PASS |
|  trackday-detail.html | PASS |
|  trackday-list.html | PASS |
|  trackday-request.html | PASS |
|  tuition-detail.html | PASS |
|  tuition.html | PASS |
|  includes/increment_decrement.html | PASS |

### /profiles

| File | Result |
| -------- | ------ |
| profile.html  | PASS |

### /home

| File | Result |
| -------- | ------ |
| about.html  | PASS |
| contact.html  | PASS |
| faqs.html  | PASS |
| index.html  | PASS |
| policies.html  | PASS |
| management.html  | PASS |
| error404.html | PASS |
| newsletter.html | PASS |

### /checkout

| File | Result |
| -------- | ------ |
| basket.html  | PASS |
| cancel.html | PASS |
| error.html | PASS |
| success.html | PASS |
| history.html | PASS |


### /cars

| File | Result |
| -------- | ------ |
| car-hire.html  | PASS |

<br/><br/> 

<details><summary> Main HTML Validation Screenshots</summary>

#### Base.html, Main-nav.html and  Index.html
![Base Template Validation](/static/images/readme-images/validation-images/base-index.html-val.png)

#### experience-detail.html
![Experience Detail Validation](/static/images/readme-images/validation-images/experience-detail.html-val.png)

#### experiences.html
![Experiences Validation](/static/images/readme-images/validation-images/experiences.html-val.png)

#### trackday-detail.html
![Trackday Detail Validation](/static/images/readme-images/validation-images/trackday-detail.html-val.png)

#### trackday-list.html
![Trackday List Validation](/static/images/readme-images/validation-images/trackday-list.html-val.png)

#### trackday-request.html
![Trackday Request Validation](/static/images//readme-images/validation-images/trackday-request.html-val.png)

#### tuition-detail.html
![Tuition Detail Validation](/static/images//readme-images/validation-images/tuition-detail.html-val.png)

#### tuition.html
![Tuition Validation](/static/images//readme-images/validation-images/tuition.html-val.png)

#### profile.html
![Profile Validation](/static/images//readme-images/validation-images/profile.html-val.png)

#### about.html
![About Validation](/static/images//readme-images/validation-images/about.html-val.png)

#### contact.html
![Contact Validation](/static/images//readme-images/validation-images/contact.html-val.png)

#### faqs.html 
![FAQS Validation](/static/images//readme-images/validation-images/faqs.html-val.png)


#### policies.html
![Policies Validation](/static/images//readme-images/validation-images/policies.html-val.png)

#### management.html
![Management Validation](/static/images//readme-images/validation-images/management.html-val.png)

#### error404.html
![Error 404 Validation](/static/images//readme-images/validation-images/error404-page-val.png)

#### newsletter.html
![Newsletter Validation](/static/images//readme-images/validation-images/newsletter.html-val.png)

#### basket.html
![Empty Basket Validation](/static/images//readme-images/validation-images/basket.html-empty-val.png)
![Full Basket Validation](/static/images//readme-images/validation-images/basket.html-with-items-val.png)

#### history.html
![Order History Validation](/static/images//readme-images/validation-images/history.html-val.png)

#### success.html
![Checkout Success Validation](/static/images//readme-images/validation-images/success.html-val.png)

#### cancel.html
![Cancel Checkout Validation](/static/images//readme-images/validation-images/cancel.html-val.png)

#### car-hire.html
![Car Hire Page Validation](/static/images//readme-images/validation-images/car-hire.html-val.png)


</details>

<br/><br/> 

### Current HTML Errors/Issues/Explanations:

- Mostly just warnings for script tags having the ` type="text/javascript" ` attribute in them. This can be ignored.

---

## CSS Validation

All CSS validation was done using https://jigsaw.w3.org/css-validator/

### /static/css

| File | Result |
| -------- | ------ |
| base.css  | PASS |


### /trackdays/css

| File | Result |
| -------- | ------ |
| booking-detail.css  | PASS  |
| exp_detail.css  | PASS  |
| experiences.css  | PASS  |
| trackday-request.css  | PASS  |
| trackdays.css  | PASS  |
| tuition.css  | PASS  |

### /profiles/css

| File | Result |
| -------- | ------ |
| profiles.css  | PASS |

### /home/css

| File | Result |
| -------- | ------ |
| about.css  | PASS |
| contact.css  | PASS |
| index.css  | PASS |
| management.css  | PASS |
| newsletter.css  | PASS |

### /basket/css

| File | Result |
| -------- | ------ |
| basket.css  | PASS |
| history.css  | PASS |

### cars/css

| File | Result |
| -------- | ------ |
| cars.css  | PASS |


<br/><br/> 

<details><summary>CSS Validation Screenshots</summary>

#### base.css
![Base CSS Validation](/static/images//readme-images/validation-images/base.css-val.png)

#### booking-detail.css
![Booking Detail CSS Validation](/static/images//readme-images/validation-images/booking-detail.css-val.png)

#### exp_detail.css
![Experience Detail CSS Validation](/static/images//readme-images/validation-images/exp_detail.css-val.png)

#### experiences.css
![Experiences CSS Validation](/static/images//readme-images/validation-images/experiences.css-val.png)

#### trackday-request.css
![Trackday Request CSS Validation](/static/images//readme-images/validation-images/trackday-request.css-val.png)

#### trackdays.css
![Trackdays CSS Validation](/static/images//readme-images/validation-images/trackdays.css-val.png)

#### tuition.css
![Tuition CSS Validation](/static/images//readme-images/validation-images/tuition.css-val.png)

#### profiles.css
![Profiles CSS Validation](/static/images//readme-images/validation-images/profiles.css-val.png)

#### about.css 
![About CSS Validation](/static/images//readme-images/validation-images/about.css-val.png)

#### contact.css
![Contact CSS Validation](/static/images//readme-images/validation-images/contact.css-val.png)

#### index.css 
![Index CSS Validation](/static/images//readme-images/validation-images/index.css-val.png)

#### management.css
![Management CSS Validation](/static/images//readme-images/validation-images/management.css-val.png)

#### newsletter.css
![Newsletter CSS Validation](/static/images//readme-images/validation-images/newsletter.css-val.png)

#### basket.css 
![Basket CSS Validation](/static/images//readme-images/validation-images/basket.css-val.png)

#### history.css
![History CSS Validation](/static/images//readme-images/validation-images/history.css-val.png)

#### cars.css
![Cars CSS Validation](/static/images//readme-images/validation-images/cars.css-val.png)

</details>

<br/><br/> 

### Current CSS Errors/Issues/Explanations:

- No issues at all to report.

---

## JS Validation

I cross-referenced JS Validation using two different Validation services:
- https://jshint.com/
- https://jsvalidator.com/

I did find this particularly useful as some files generated warnings on one validator (perhaps due to over-sensitivity) and passed with zero errors on another.
I have included different screenshots to demonstrate this and show that the JS is valid and working.


### profiles/js

| File | Result |
| -------- | ------ |
| profile.js | PASS |

### home/js

| File | Result |
| -------- | ------ |
| base.js  | PASS |

<br/><br/> 

<details><summary>JS Validation Screenshots</summary>

#### profile.js
![Profile Page JS](/static/images/readme-images/validation-images/profiles.js-val.png)

#### base.js
![Base JS](/static/images//readme-images/validation-images/base.js-val.png)
![Base JS](/static/images//readme-images/validation-images/base.js-js-val.png)

#### increment-decrement js
![Increment and Decrement JS](/static/images/readme-images/validation-images/increment-decrement-script-js-val.png)

#### basket js
![Basket JS](/static/images/readme-images/validation-images/basket-js-script-val.png)

#### Management js
![Management JS](/static/images/readme-images/validation-images/management-js-script-val.png)

#### Trackday Detail js
![Trackday Detail JS](/static/images/readme-images/validation-images/trackday-detail-js-script-val.png)

#### Bootstrap Toast js
![Bootstrap Toast JS](/static/images/readme-images/validation-images/bootstrap-toasts-js-val.png)
![Bootstrao Toast JS](/static/images/readme-images/validation-images/bootstrap-toasts-js-js-val.png)


</details>

<br/><br/> 

### Current JS Errors/Issues/Explanations:

- As you can see from the screen shots, the same code on one js linter can be more sensitive towards things than others. I have included cases like this above for transparency and to prove I have tested across more than one JS linter.


---

## Python Validation

All Python validation was checked through Code Institute's PEP8 Python Linter. You can find it via this link: https://pep8ci.herokuapp.com/

### /django_raceway


| File | Result |
| -------- | ------ |
| settings.py | PASS |
| urls.py | PASS |


### /trackdays

| File | Result |
| -------- | ------ |
| admin.py | PASS |
| models.py | PASS |
| urls.py | PASS |
| views.py | PASS |
| tests.py |  |



### /profiles

| File | Result |
| -------- | ------ |
| admin.py | PASS |
| models.py | PASS |
| urls.py | PASS |
| views.py | PASS |
| tests.py |  |



### /home

| File | Result |
| -------- | ------ |
| admin.py | PASS |
| models.py | PASS |
| urls.py | PASS |
| views.py | PASS |
| tests.py |  |



### /checkout

| File | Result |
| -------- | ------ |
| admin.py | PASS |
| contexts.py | PASS |
| models.py | PASS |
| urls.py | PASS |
| views.py | PASS* |
| helpers.py | PASS |
| tests.py |  |

* Line 320 in views.py reads as too long, however, for reliability I have opted to leave this
in as it can cause issues in deployment when concatenated as it is a url. I believe this is
a sensible and reasonable precaution to take for site reliability.


### /cars

| File | Result |
| -------- | ------ |
| admin.py | PASS |
| models.py | PASS |
| urls.py | PASS |
| views.py | PASS |
| tests.py | PASS |

<br/><br/> 

<details><summary>Python Validation Screenshots</summary>

#### /django_raceway

![settings.py](/static/images/readme-images/validation-images/django_raceway-settings.py-val.png)
![urls.py](/static/images/readme-images/validation-images/django_raceway-urls.py-val.png)


#### /trackdays

![admin.py](/static/images/readme-images/validation-images/trackdays-admin.py-val.png)
![models.py](/static/images/readme-images/validation-images/trackdays-models.py-val.png)
![urls.py](/static/images/readme-images/validation-images/trackdays-urls.py-val.png)
![views.py](/static/images/readme-images/validation-images/trackdays-views.py-val.png)


#### /home

![admin.py](/static/images/readme-images/validation-images/home-admin.py-val.png)
![models.py](/static/images/readme-images/validation-images/home-models.py-val.png)
![urls.py](/static/images/readme-images/validation-images/home-urls.py-val.png)
![views.py](/static/images/readme-images/validation-images/home-views.py-val.png)


#### /profiles

![admin.py](/static/images/readme-images/validation-images/profiles-admin.py-val.png)
![models.py](/static/images/readme-images/validation-images/profiles-models.py-val.png)
![urls.py](/static/images/readme-images/validation-images/profiles-urls.py-val.png)
![views.py](/static/images/readme-images/validation-images/profiles-views.py-val.png)

#### /checkout

![admin.py](/static/images/readme-images/validation-images/checkout-admin.py-val.png)
![models.py](/static/images/readme-images/validation-images/checkout-models.py-val.png)
![urls.py](/static/images/readme-images/validation-images/checkout-urls.py-val.png)
![views.py](/static/images/readme-images/validation-images/checkout-views.py-val.png)
![views.py 2](/static/images/readme-images/validation-images/checkout-views.py-line-length.png)
![contexts.py](/static/images/readme-images/validation-images/checkout-contexts.py-val.png)
![helpers.py](/static/images/readme-images/validation-images/checkout-helpers.py-val.png)


#### /cars

![admin.py](/static/images/readme-images/validation-images)
![models.py](/static/images/readme-images/validation-images)
![urls.py](/static/images/readme-images/validation-images)
![views.py](/static/images/readme-images/validation-images)
![tests.py](/static/images/readme-images/validation-images)


</details>

<br/><br/> 

### Current Python Errors/Issues/Explanations:

- Only 1 known python linting issue across the entire workspace, being that of line 320 in /checkout/views.py where a line is too long by 2 characters.
Due to this being a url, and a pretty specific one from Stripe as well, I opted to follow best practice and to leave it as is for this one exception in order 
to ensure reliability of the checkout on the site. I believe reliability takes priority over anything else.


---

## Lighthouse Performance Testing

- Lighthouse Testing was performed in an incognito tab to ensure no external chrome add-ons were affecting the test.
- Results of the Lighthouse Performance testing below:

Lighthouse Screeshot here: xxxxxxxxxxxxxx

---

## Device and Browser Testing

- Browsers Tested:
    - Google Chrome
    - Safari

- Devices Tested:
    - MacBook Pro
    - Apple iPhone 12 Pro
    - iPhone 14 Pro
    - iPhone X
    - iPad Pro



### Responsiveness

- The site has been tested down to screen widths of 320px and up to screen widths of 2560px
- The site is fully responsive between these viewport widths

---


## Current known and unresolved issues

- As documented in the outstanding bugs section in the readme, there is an (as of writing) unresolved bug where when you sign in or log out, the sign in and log out buttons appear to not be clickable. This is always able to be fixed by either refreshing the page or clicking on to another link/page. Alternatively, click on the site logo (which redirects to the home page anyway) to clear this bug. 
- My Trackday Constraint in my Trackday model appears to not work realiably. I have tried various combinations of the code, tried to reformat it countless times and tried to use it in conjunction with adding ` unique=True` in the fields that are supposed to work with it. I have yet to resolve this issue and will aim to do so in a future update.
- 


--- 

[Return to Top](#manual-and-automated-testing)