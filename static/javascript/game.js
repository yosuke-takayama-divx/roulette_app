// WebSocketの初期化(https=wss)
const socket = new WebSocket(
    'wss://' + window.location.host + '/ws/roulette/'
);
let results = {};
let currentIndex = null;

socket.onopen = function() {
    console.log("WebSocket接続が開かれました。");
};

socket.onmessage = function(e) {
    const data = JSON.parse(e.data);

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

            // 選ばれた武器一覧更新
            const listResultName = document.getElementById("list_resultName" + data.index);
            listResultName.innerText = userName + 'の武器は ' + data.image_name + ' です！';

            // 現在のインデックス更新
            if (currentIndex === data.index) {
                updateResultDisplay(data.index);
            }

            // フォームデータ更新
            if (data.formData) {
                for (let i = 1; i <= 10; i++) {
                    const input = document.getElementById("userName" + i);
                    if (input) {
                        input.value = data.formData["userName" + i] || "";
                    }
                }
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

    console.log("スピンボタンが押されました"); // デバッグ用ログ

    // WebSocketが開いているか確認
    if (socket.readyState === WebSocket.OPEN) {
        // 各入力フィールドの値を取得して送信
        for (let i = 1; i <= 10; i++) {
            const userNameInput = document.getElementById("userName" + i);
            const userName = userNameInput ? userNameInput.value || "あなた" : "あなた";
            console.log(`送信するデータ: ${JSON.stringify({ userName: userName, index: i })}`); // デバッグ用ログ
            socket.send(JSON.stringify({ userName: userName, index: i }));
        }
    } else {
        console.error("WebSocketはオープンではありません。状態：" + socket.readyState);
    }
}
// 結果表示ボタン
function showResult(index) {
    const result = results[index];
    const errorMessage = document.getElementById("errorMessage");
    if (result) {
        updateResultDisplay(index);
        currentIndex = index;
        errorMessage.innerText = "";
    } else {
        errorMessage.innerText = `${index} のルーレットを登録しました`;
    }
}

// 結果表示を更新する関数
function updateResultDisplay(index) {
    const result = results[index];
    const img = document.getElementById("resultImage");
    const name = document.getElementById("resultName");
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
