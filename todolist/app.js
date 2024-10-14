// DOM要素の取得
const taskForm = document.getElementById('task-form');
const taskInput = document.getElementById('task-input');
const taskList = document.getElementById('task-list');

// APIのベースURL（自分のAPIのURLに置き換えてね）
const API_BASE_URL = 'https://51venj3nph.execute-api.ap-northeast-1.amazonaws.com/prod';

// タスクを取得する関数
async function fetchTasks() {
    const response = await fetch(`${API_BASE_URL}/tasks`);
    const data = await response.json();
    return data.Items || [];
}

// タスクを追加する関数
async function addTask(task) {
    const response = await fetch(`${API_BASE_URL}/tasks`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(task),
    });
    return response.ok;
}

// タスクを表示する関数
function renderTask(task) {
    const li = document.createElement('li');
    li.innerHTML = `
        <input type="checkbox" ${task.completed ? 'checked' : ''}>
        <span>${task.text}</span>
        <button class="delete-btn">削除</button>
    `;
    taskList.appendChild(li);
}

// 初期化関数
async function init() {
    const tasks = await fetchTasks();
    tasks.forEach(renderTask);
}

// フォームの送信イベントリスナー
taskForm.addEventListener('submit', async function(e) {
    e.preventDefault();
    const taskText = taskInput.value.trim();
    if (taskText !== '') {
        const task = {
            id: Date.now().toString(),
            text: taskText,
            completed: false
        };
        const success = await addTask(task);
        if (success) {
            renderTask(task);
            taskInput.value = '';
        } else {
            alert('タスクの追加に失敗しました');
        }
    }
});

// 初期化
init();