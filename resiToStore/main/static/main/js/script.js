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

    <div class="signUp">
    <div class="closeBtn">&times;</div>
    <div class="formReg">
        <h2>Регистрация</h2>
        <div class="formRegElement">
            <label for="emailReg">Почта</label>
            <input type="text" id="emailReg" placeholder="example@gmail.com">
        </div>
        <div class="formRegElement">
            <label for="passwordReg">Пароль</label>
            <input type="password" id="passwordReg" placeholder="Пароль">
        </div>
        <div class="formRegElement">
            <label for="passwordRegRepeat">Повторите пароль</label>
            <input type="password" id="passwordRegRepeat" placeholder="Повторите пароль">
        </div>
        <div class="formRegElement">
            <button class="signUpBtn">Регистрация</button>
        </div>
    </div>
</div>l>
`;

document.body.insertAdjacentHTML('beforeend', htmlTemplate);

document.getElementById("show-login").addEventListener('click', function() {
    document.querySelector(".signIn").classList.add("activate");
});

document.querySelector(".signIn .closeBtn").addEventListener('click', function() {
    document.querySelector(".signIn").classList.remove("activate");
});

document.getElementById("show-reg").addEventListener('click', function() {
    document.querySelector(".signUp").classList.add("activate");
});

document.querySelector(".signUp .closeBtn").addEventListener('click', function() {
    document.querySelector(".signUp").classList.remove("activate");
});
