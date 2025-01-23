let timer;
let startTime;
let isRunning = false;
let pieceCount = 0;

const timerDisplay = document.getElementById('timer');
const startBtn = document.getElementById('startBtn');
const stopBtn = document.getElementById('stopBtn');
const led = document.getElementById('led');
const buzzer = document.getElementById('buzzer');

function formatTime(ms) {
    const minutes = Math.floor(ms / 60000);
    const seconds = Math.floor((ms % 60000) / 1000);
    const deciseconds = Math.floor((ms % 1000) / 100);
    return `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}.${deciseconds}`;
}

function updateTimer() {
    const currentTime = Date.now();
    const elapsedTime = currentTime - startTime;
    timerDisplay.textContent = formatTime(elapsedTime);

    // Check alerts
    if (elapsedTime >= 32000) {
        led.classList.add('active');

        if (elapsedTime >= 35000) {
            buzzer.classList.add('active');
        }
    }
}

function startTimer() {
    startTime = Date.now();
    isRunning = true;
    timer = setInterval(updateTimer, 100);

    startBtn.disabled = true;
    stopBtn.disabled = false;
    led.classList.remove('active');
    buzzer.classList.remove('active');
}

function stopTimer() {
    clearInterval(timer);
    isRunning = false;

    startBtn.disabled = false;
    stopBtn.disabled = true;

    // Add to history
    const duration = Date.now() - startTime;
    addToHistory(duration);

    // Reset alerts
    led.classList.remove('active');
    buzzer.classList.remove('active');
}

function addToHistory(duration) {
    pieceCount++;
    const row = document.createElement('tr');

    const status = duration >= 35000 ? 'Overcooked' :
                   duration >= 32000 ? 'Warning' : 'Normal';

    row.innerHTML = `
        <td>${pieceCount}</td>
        <td>${formatTime(duration)}</td>
        <td>${new Date().toLocaleString()}</td>
        <td>${status}</td>
    `;

    const tbody = document.getElementById('historyTable');
    tbody.insertBefore(row, tbody.firstChild);

    // Save to backend
    saveRecord(duration, status);
}

async function saveRecord(duration, status) {
    try {
        const response = await fetch('/api/records', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                duration: duration,
                status: status,
                timestamp: new Date().toISOString()
            })
        });

        if (!response.ok) {
            console.error('Failed to save record');
        }
    } catch (error) {
        console.error('Error saving record:', error);
    }
}

startBtn.addEventListener('click', startTimer);
stopBtn.addEventListener('click', stopTimer);
