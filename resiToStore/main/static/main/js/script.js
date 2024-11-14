
const htmlTemplate = `
    <div class="signIn">
        <div class="closeBtn">&times;</div>
        <div class="form">
            <h2>Вход</h2>
            <div class="formElement">
                <label for="email">Почта</label>
                <input type="text" id="email" placeholder="example@gmail.com">
            </div>
            <div class="formElement">
                <label for="password">Пароль</label>
                <input type="password" id="password" placeholder="Пароль">
            </div>
            <div class="formElement">
                <button class="standartButton">Вход</button>
            </div>
            <div class="formElement">
                <a href="#">Забыли пароль</a>
            </div>
        </div>
    </div>
`;

document.body.insertAdjacentHTML('beforeend', htmlTemplate);

document.getElementById("show-login").addEventListener('click', function() {
    document.querySelector(".signIn").classList.add("activate");
});

document.querySelector(".signIn .closeBtn").addEventListener('click', function() {
    document.querySelector(".signIn").classList.remove("activate");
});
