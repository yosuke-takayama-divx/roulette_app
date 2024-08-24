const socket = new WebSocket('ws://' + window.location.host + '/ws/roulette/');
let results = {};
let currentIndex = null;

socket.onopen = function() {
    console.log("WebSocket接続が開かれました。");
};

socket.onmessage = function(e) {
    const data = JSON.parse(e.data);

    // data.indexがundefinedでないことを確認
    if (data.index !== undefined) {
        const userNameInput = document.getElementById("userName" + data.index);

        if (userNameInput) {
            const userName = userNameInput.value || "あなた";

            // 結果を保存
            results[data.index] = {
                userName: userName,
                imageName: data.image_name,
                imagePath: data.image_path
            };

            // 選ばれた武器一覧を更新
            const listResultName = document.getElementById("list_resultName" + data.index);
            listResultName.innerText = userName + 'の武器は ' + data.image_name + ' です！';

            // 現在のインデックスを更新
            if (currentIndex === data.index) {
                updateResultDisplay(data.index);
            }
        } else {
            console.error("userName" + data.index + " が見つかりません。");
        }
    } else {
        console.error("data.index が undefined です。");
    }
};

socket.onerror = function(error) {
    console.error("WebSocketエラーが発生しました：", error);
};

socket.onclose = function() {
    console.log("WebSocket接続が閉じられました。");
};

// スピンボタン
function spinRoulette(event) {
    // ページリロード防止
    event.preventDefault();

    // 各入力フィールドの値を取得して送信
    for (let i = 1; i <= 10; i++) {
        const userNameInput = document.getElementById("userName" + i);
        const userName = userNameInput ? userNameInput.value || "あなた" : "あなた";
        socket.send(JSON.stringify({ userName: userName, index: i }));
    }
}

// 結果表示ボタン
function showResult(index) {
    const result = results[index];
    const errorMessage = document.getElementById("errorMessage");
    if (result) {
        updateResultDisplay(index);
        currentIndex = index;
        errorMessage.innerText = ""; // エラーメッセージをクリア
    } else {
        errorMessage.innerText = "スピンボタンを押してください。";
    }
}

// 結果表示を更新する関数
function updateResultDisplay(index) {
    const result = results[index];
    const img = document.getElementById("resultImage");
    const name = document.getElementById("resultName");
    
    // STATIC_URL がどこで定義されているかを確認してください
    img.src = STATIC_URL + result.imagePath;
    name.innerText = result.userName + 'の武器は ' + result.imageName + ' です！';
}

// ページがロードされた時0.jpgを表示
document.addEventListener("DOMContentLoaded", function() {
    const img = document.getElementById("resultImage");
    img.src = STATIC_URL + "images/0.jpg";
});

document.getElementById("btn_form_wrap").onclick = function() {
    const formWrap = document.getElementById("form_wrap");
    formWrap.classList.toggle("toggle_open");
};

// スピンボタンのクリックハンドラーを設定
document.getElementById("spinButton").onclick = spinRoulette;  // スピンボタンのIDを確認
