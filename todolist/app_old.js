// DOM要素の取得
const taskForm = document.getElementById('task-form');
const taskInput = document.getElementById('task-input');
const taskList = document.getElementById('task-list');

// タスクの配列
let tasks = [];

// フォームの送信イベントリスナー
taskForm.addEventListener('submit', function(e) {
    e.preventDefault(); // フォームのデフォルト送信を防ぐ
    addTask();
});

// タスクを追加する関数
function addTask() {
    const taskText = taskInput.value.trim();
    if (taskText !== '') {
        const task = {
            id: Date.now(),
            text: taskText,
            completed: false
        };
        tasks.push(task);
        renderTask(task);
        taskInput.value = '';
    }
}

// タスクを画面に表示する関数
function renderTask(task) {
    const li = document.createElement('li');
    li.setAttribute('data-id', task.id);
    li.innerHTML = `
        <input type="checkbox" ${task.completed ? 'checked' : ''}>
        <span>${task.text}</span>
        <button class="delete-btn">削除</button>
    `;
    
    // チェックボックスのイベントリスナー
    const checkbox = li.querySelector('input[type="checkbox"]');
    checkbox.addEventListener('change', function() {
        toggleTask(task.id);
    });
    
    // 削除ボタンのイベントリスナー
    const deleteBtn = li.querySelector('.delete-btn');
    deleteBtn.addEventListener('click', function() {
        deleteTask(task.id);
    });
    
    taskList.appendChild(li);
}

// タスクの完了状態を切り替える関数
function toggleTask(id) {
    const task = tasks.find(t => t.id === id);
    task.completed = !task.completed;
}

// タスクを削除する関数
function deleteTask(id) {
    tasks = tasks.filter(t => t.id !== id);
    const li = taskList.querySelector(`[data-id="${id}"]`);
    li.remove();
}