پروژه نهایی
----
ابتدا استخراج دیتا از سایت مورد نظر، سپس ایجاد دیتا بیس و وارد کردن دیتاها به دیتابیس
در انتخا خواندن دیتا ها و ایجاد یک مدل ماشین لرنینگ برای پیشبینی قیمت کالا 


*** راه حل ***
برای این پروژه ما سایت truecar رو انتخاب کردیم و دلایل این انتخاب هم {1- وجود دیتا فراوان برای تمرین و ایجاد ماشین لرنینگ 2- وجود دیتا کامل و یکنواخت برای هر ایتم 3-زیاد نبودن کدهای جاوا اسکریپت که اسکریپ سایت رو راحت تر میکنه)
با توجه به سایت و اطلاعات مورد نیاز، در دو اسکریپ Database و DB_Setup ابتدا به ایجاد و تنظیم دیتابیس می پردازیم 
بعد از ایجاد دیتابیس و توابع مورد نیاز ان ، در اسکریپت scrape به اسکریپ سایت truecar میپردازیم و اطلاعات مورد نیاز رو از این سایت استخراج و به دیتابیس تزریق میکنیم.
در ادامه در اسکریپت ML ابتدا دیتا های مورد نیاز رو از دیتابیس خوانده و به ایجاد مدل ماشین لرنینگ خود می پردازیم.
مدل انتخابی ما  DecisionTreeRegressor از بین مدلهای  [LinearRegression,KNeighborsRegressor,DecisionTreeRegressor,LogisticRegression] بود, که این مدل بهترین جواب های ممکن رو پیش بینی می‌کرد.
برای اسکیل کردن اطلاعات ورودی از QuantileTransformer استفاده کردیم که توزیع مناسبی ایجاد میکنه و برای کد کردن استرینگ ها از LabelEncoder استفاده کردیم. 
سپس با استفاده از f_regression  مقادیر p_value رو برای featureهای بدست اوردیم که feature های لازم رو حفظ و مابقی رو برای داشتن مدلی بهتر حذف کنیم. در مورد مدل ما که به پیشبینی قیمت ماشین می پردازه رنگ ماشین feature بود
که ان را حذف کردیم چرا که مقدار p_value آن حدود 0.4 بود که نشان از عدم اهمیت آن در مدل ما برای پیش بینی قیمت بود.
سپس مدل روبا استفاده از pipeline و gridsearch ساختیم و در انتها با ایجاد یک تابع که از مدل ساخته شده استفاده میکرد به پیش بینی قیمت ماشین که هدف ما بود رسیدیم.
 مدل ما قابل به پیش بینی قیمت تقریبی ماشین هایی هست که قبل مدل آنها را دیده است (با توجه به محدودیت labelencoder) لذا در صورتی که مدل ورودی در لیست تمرین داده شده نباشد، لیست از مدل هایی که قابل پیش بینی است به شما نشان داده می شود.

پ‌ن: نام مدل وارد شده باید مطابق با نام موجود در لیست باشد (محدودیت های labelencoder)

GitHub
https://github.com/aminoffline/ad-python-final_project.git