console.log("Dashboard Loaded");

/* =========================================
   DYNAMIC GREETING
========================================= */

function updateGreeting() {

    const greetingText =
        document.getElementById("greetingText");

    if (!greetingText) return;

    const hour = new Date().getHours();

    let greeting = "";

    if (hour >= 5 && hour < 12) {

        greeting = "Good Morning ☀️";

    }

    else if (hour >= 12 && hour < 17) {

        greeting = "Good Afternoon 🌤️";

    }

    else if (hour >= 17 && hour < 21) {

        greeting = "Good Evening 🌇";

    }

    else {

        greeting = "Good Night 🌙";

    }

    greetingText.innerText = greeting;
}

updateGreeting();

/* =========================================
   DAILY QUOTES
========================================= */

const quotes = [

    "Take care of your body. It’s the only place you have to live.",

    "Every medicine works better with a positive mindset.",

    "Small healthy habits make a big difference.",

    "Health is the real wealth.",

    "Stay hydrated and stay strong.",

    "A healthy life starts with discipline.",

    "Consistency is the key to good health."

];

const quoteText =
    document.getElementById("quoteText");

if (quoteText) {

    const randomQuote =
        quotes[Math.floor(Math.random() * quotes.length)];

    quoteText.innerText = randomQuote;
}

/* =========================================
   HEALTH TIPS
========================================= */

const tips = [

    "Drink enough water and maintain proper sleep.",

    "Take medicines on time for better recovery.",

    "Daily walking improves heart health.",

    "Avoid skipping meals during medication.",

    "Meditation reduces stress and improves focus.",

    "Exercise daily for at least 30 minutes."

];

const healthTip =
    document.getElementById("healthTip");

if (healthTip) {

    const randomTip =
        tips[Math.floor(Math.random() * tips.length)];

    healthTip.innerText = randomTip;
}

/* =========================================
   WATER TRACKER
========================================= */

let waterCount =
    parseInt(localStorage.getItem("waterCount")) || 0;

const waterCountText =
    document.getElementById("waterCount");

const progressBar =
    document.getElementById("waterProgressBar");

function updateWaterUI() {

    if (!waterCountText || !progressBar) return;

    waterCountText.innerText =
        `${waterCount} / 8 Glasses`;

    const percentage =
        (waterCount / 8) * 100;

    progressBar.style.width =
        `${percentage}%`;
}

function drinkWater() {

    if (waterCount < 8) {

        waterCount++;

        localStorage.setItem(
            "waterCount",
            waterCount
        );

        updateWaterUI();
    }
}

updateWaterUI();

/* =========================================
   WATER REMINDER
========================================= */

if ("Notification" in window) {

    Notification.requestPermission();

    setInterval(() => {

        if (Notification.permission === "granted") {

            new Notification(
                "💧 Water Reminder",
                {
                    body:
                        "Time to drink water and stay hydrated!"
                }
            );
        }

    }, 3600000);
}