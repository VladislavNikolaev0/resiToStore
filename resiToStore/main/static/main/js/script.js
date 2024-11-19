//var pathToLogin = ""
//var csrf_token = ""
//
//const htmlTemplate = `
//    <div class="signIn">
//    <div class="closeBtn">&times;</div>
//    <div class="form">
//        <form method="POST" action=` + pathToLogin + `>
//        ` + csrf_token + `
//        <h2>Вход</h2>
//        <div class="formElement">
//            <label for="login">Почта</label>
//            <input type="text" id="login" name="login" placeholder="login">
//        </div>
//        <div class="formElement">
//            <label for="password">Пароль</label>
//            <input type="password" id="password" name="password" placeholder="Пароль">
//        </div>
//
//        <div class="formElement">
//            <button class="signInBtn" type="submit">Вход</button>
//        </div>
//        <div class="formElement">
//            <a class="forgotPassword" href="#">Забыли пароль</a>
//        </div>
//        </form>
//    </div>
//</div>
//
//    <div class="signUp">
//    <div class="closeBtn">&times;</div>
//    <div class="formReg">
//        <h2>Регистрация</h2>
//        <div class="formRegElement">
//            <label for="emailReg">Почта</label>
//            <input type="text" id="emailReg" name="login" placeholder="example@gmail.com">
//        </div>
//        <div class="formRegElement">
//            <label for="passwordReg">Пароль</label>
//            <input type="password" id="passwordReg" name="password" placeholder="Пароль">
//        </div>
//        <div class="formRegElement">
//            <label for="passwordRegRepeat">Повторите пароль</label>
//            <input type="password" id="passwordRegRepeat" name="repeatPassword" placeholder="Повторите пароль">
//        </div>
//        <div class="formRegElement">
//            <button class="signUpBtn">Регистрация</button>
//        </div>
//    </div>
//</div>l>
//`;
//
//document.body.insertAdjacentHTML('beforeend', htmlTemplate);
//
//document.getElementById("show-login").addEventListener('click', function() {
//    console.log(pathToLogin)
//    console.log(csrf_token)
//    document.querySelector(".signIn").classList.add("activate");
////    history.pushState(null, '', '/users/login');
//});
//
//document.querySelector(".signIn .closeBtn").addEventListener('click', function() {
//    document.querySelector(".signIn").classList.remove("activate");
//});
//
//document.getElementById("show-reg").addEventListener('click', function() {
//    document.querySelector(".signUp").classList.add("activate");
//    history.pushState(null, '', '/users/register');
//});
//
//document.querySelector(".signUp .closeBtn").addEventListener('click', function() {
//    document.querySelector(".signUp").classList.remove("activate");
//});