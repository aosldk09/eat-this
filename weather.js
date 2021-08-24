function good() {
    alert("좋아 이걸로 결정!!")
}

function bad() {
    alert("다른걸로 추천ㄱㄱ!!")
}

function weather_bg(weather) {
    if (weather == 'Rain') {
        document.body.style.backgroundImage = "url(/static/rain.jpg)";
    } else if (weather == 'Clouds') {
        document.body.style.backgroundImage = "url(/static/cloud.jpg)";
    } else if (weather == 'Clean') {
        document.body.style.backgroundImage = "url(/static/clean.jpg)";
    } else if (weather == 'Dust') {
        document.body.style.backgroundImage = "url(/static/mise.jpg)";
    }
}


let rainFood = ['모둠전', '우동', '어묵탕', '돌솥비빔밥', '두부김치'];
let cloudsFood = ['설렁탕', '갈비탕', '감자탕', '국밥', '찌개'];
let dustFood = ['삼겹살', '소곱창', '돈까스', '피자', '곱창전골'];
let clearFood = ['냉면', '비빔면', '냉모밀', '삼계탕', '물회'];
let food = '';

function chooseFood(weather) {
    let rd = Math.floor(Math.random() * 5);
    switch (weather) {
        case 'Rain':
            //rain이 맞으면
            food = rainFood[rd];
            console.log(food)
            $('#food-js').append(food)
            break;
        case 'Clouds':
            //clouds가 맞으면
            food = cloudsFood[rd];
            console.log(food)
            $('#food-js').append(food)
            break;
        case 'Dust':
            //dust가 맞으면
            food = dustFood[rd];
            console.log(food)
            $('#food-js').append(food)
            break;
        case 'Clear':
            //clear가 맞으면
            food = clearFood[rd];
            console.log(food)
            $('#food-js').append(food)
            break;
    }
}

// initialize
async function initWeatherInfo(latitude, longitude) {
    console.log('position', latitude, longitude)
    try {
        const response = await requestWeather(latitude, longitude)
        setWeather(response)
        chooseFood(response.weather[0].main)
        weather_bg(response.weather[0].main)
    } catch (err) {
        console.error(err)
    }
}

// 날씨 정보 요청
function requestWeather(latitude, longitude) {
    return new Promise((resolve, reject) => {
        const apiKey = "8e3a8d4780bc10f08f39acedc17cff21"
        const weatherUrl = "https://api.openweathermap.org/data/2.5/weather?lat=" + latitude
            + "&lon=" + longitude
            + "&appid=" + apiKey + "&units=metric";
        $.ajax({
            url: weatherUrl,
            type: 'GET',
            dataType: 'json',
            success: (response) => {
                console.log('weatherInfo', response)
                resolve(response)
            },
            error: () => {
                reject(new Error(error))
            }
        })
    })
}

// 날씨 셋팅
function setWeather(weatherInfo) {
    $('#weather-js').append(weatherInfo.weather[0].main)
    $('#temp-js').append(weatherInfo.main.temp)
    $('#cityname-js').append(weatherInfo.name)
}

// 위치 권한 허용창
function requestPopup() {
    const result = window.confirm('위치 권한을 허용하시겠습니까?')
    setAuthority(result)
}

//위치 정보 셋팅
function setAuthority(result) {
    console.log('위치 권한 허용 여부', result)
    result ? navigator.geolocation.getCurrentPosition((res) => {
        initWeatherInfo(res.coords.latitude, res.coords.longitude)
    }, (err) => {
        console.error(err)
        initWeatherInfo(37.5577074, 126.9766557)
    }) : initWeatherInfo(37.5577074, 126.9766557)
}


window.addEventListener('load', () => {
    requestPopup()
    //setAuthority(true)
})