// WebSocketのプロトコルを設定
const protocol = window.location.protocol === 'https:' ? 'wss://' : 'ws://';
const socket = new WebSocket(protocol + window.location.host + '/ws/roulette/'); // WebSocket接続を確立

let results = {}; // 結果を保存するためのオブジェクト
let currentIndex = null; // 現在選ばれているインデックス

// WebSocket接続が開かれた際の処理
socket.onopen = function() {
    console.log("WebSocket接続が開かれました。");
};

// WebSocketメッセージ受信時の処理
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

            // 選ばれた武器の表示を更新
            const listResultName = document.getElementById("list_resultName" + data.index);
            listResultName.innerText = userName + 'の武器は ' + data.image_name + ' です！';

            // 現在のインデックスの結果を表示
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

// WebSocket接続エラー時の処理
socket.onerror = function(error) {
    console.error("WebSocketエラーが発生しました：", error);
};

// WebSocket接続が閉じられた際の処理
socket.onclose = function() {
    console.log("WebSocket接続が閉じられました。");
};

// ルーレットを回す関数
function spinRoulette(event) {
    event.preventDefault(); // ページリロード防止
    if (socket.readyState === WebSocket.OPEN) { // WebSocketがオープンな状態であれば
        for (let i = 1; i <= 10; i++) {
            const userNameInput = document.getElementById("userName" + i);
            const userName = userNameInput ? userNameInput.value || "あなた" : "あなた";
            socket.send(JSON.stringify({ userName: userName, index: i })); // データを送信
        }
    } else {
        console.error("WebSocketは接続されていないため、メッセージを送信できません。");
    }
}

// 結果を表示する関数
function showResult(index) {
    const result = results[index]; // 結果を取得
    const errorMessage = document.getElementById("errorMessage");
    if (result) {
        updateResultDisplay(index); // 結果を表示
        currentIndex = index; // 現在のインデックスを更新
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
    img.src = STATIC_URL + result.imagePath; // 画像パスを設定
    name.innerText = result.userName + 'の武器は ' + result.imageName + ' です！'; // 名前と武器を表示
}

// ページが読み込まれた際の初期処理
document.addEventListener("DOMContentLoaded", function() {
    const img = document.getElementById("resultImage");
    img.src = STATIC_URL + "images/0.jpg"; // 初期画像を設定
    document.getElementById("spinButton").onclick = spinRoulette; // スピンボタンのクリックハンドラーを設定
});

// フォームを表示・非表示にするボタンの処理
document.getElementById("btn_form_wrap").onclick = function() {
    const formWrap = document.getElementById("form_wrap");
    formWrap.classList.toggle("toggle_open"); // フォームの表示状態を切替
};
