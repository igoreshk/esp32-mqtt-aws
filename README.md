<div class="container">
    <main class="main-content">
        <section class="card">
            <h2>📁 Содержание репозитория</h2>
            <p>В репозитории находятся несколько файлов с кодом для ESP32:</p>
            
            <table>
                <thead>
                    <tr>
                        <th>Файл</th>
                        <th>Назначение</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>esp-aws-mqtt.ino</strong></td>
                        <td>Основной скетч для подключения к AWS IoT Core через MQTT</td>
                    </tr>
                    <tr>
                        <td><strong>esp32_mqtt_cons.ino</strong></td>
                        <td>Пример MQTT-клиента (Consumer)</td>
                    </tr>
                    <tr>
                        <td><strong>esp32_mqtt_serv.ino</strong></td>
                        <td>Пример MQTT-сервера (Broker)</td>
                    </tr>
                    <tr>
                        <td><strong>esp32_BLE_switchstatusreceived.ino</strong></td>
                        <td>Обработчик статуса BLE-переключателя</td>
                    </tr>
                    <tr>
                        <td><strong>esp32_iBeacon_servicedata_deepsleep_test.ino</strong></td>
                        <td>Тест для iBeacon, работы с сервисными данными и режима глубокого сна</td>
                    </tr>
                    <tr>
                        <td><strong>aws_alpn_gatt.py</strong></td>
                        <td>Вспомогательный скрипт на Python для работы с ALPN и GATT</td>
                    </tr>
                </tbody>
            </table>
        </section>
        
        <section class="card">
            <h2>🎯 Основные возможности</h2>
            <ul class="file-list">
                <li><strong>Безопасное облако</strong>: Подключение к AWS IoT Core с аутентификацией по сертификату X.509</li>
                <li><strong>Работа с Bluetooth</strong>: Сканирование и взаимодействие с BLE-устройствами (например, iBeacon)</li>
                <li><strong>Энергоэффективность</strong>: Реализация режима глубокого сна для автономной работы</li>
                <li><strong>Роль шлюза</strong>: Преобразование данных с BLE-устройств в MQTT-сообщения для отправки в облако</li>
            </ul>
        </section>
        
        <section class="card">
            <h2>🛠 Технологии</h2>
            <p><strong>Целевая платформа:</strong> Микроконтроллер ESP32</p>
            <p><strong>Языки программирования:</strong></p>
            <span class="tech-badge">C++ (основная прошивка)</span>
            <span class="tech-badge">Python (вспомогательные утилиты)</span>
            
            <p style="margin-top: 15px;"><strong>Ключевые протоколы:</strong></p>
            <span class="tech-badge">MQTT через TLS</span>
            <span class="tech-badge">Bluetooth Low Energy (BLE/GATT)</span>
        </section>
        
        <section class="card">
            <h2>🚀 Быстрый старт (основные шаги)</h2>
            
            <div class="step">
                <div class="step-number">1</div>
                <div class="step-content">
                    <h3>Подготовка окружения</h3>
                    <p>Установите Arduino IDE или PlatformIO с поддержкой плат ESP32</p>
                </div>
            </div>
            
            <div class="step">
                <div class="step-number">2</div>
                <div class="step-content">
                    <h3>Настройка AWS</h3>
                    <p>Зарегистрируйте "Вещь" (Thing) в сервисе AWS IoT Core, сгенерируйте и скачайте сертификаты устройства (X.509), прикрепите необходимую политику доступа (IAM Policy)</p>
                </div>
            </div>
            
            <div class="step">
                <div class="step-number">3</div>
                <div class="step-content">
                    <h3>Настройка устройства</h3>
                    <p>Укажите параметры вашей WiFi-сети (SSID, пароль), добавьте в код данные вашего AWS-аккаунта (эндпоинт, сертификаты, приватный ключ)</p>
                </div>
            </div>
            
            <div class="step">
                <div class="step-number">4</div>
                <div class="step-content">
                    <h3>Прошивка и запуск</h3>
                    <p>Скомпилируйте проект и загрузите его на плату ESP32</p>
                </div>
            </div>
        </section>
        
        <section class="card">
            <h2>💡 Примеры использования</h2>
            <ul class="file-list">
                <li><strong>Умный дом</strong>: Шлюз для подключения BLE-датчиков (температуры, влажности, датчиков открытия) к облачной платформе AWS</li>
                <li><strong>Отслеживание активов</strong>: Мониторинг местоположения меток iBeacon с передачей данных в AWS для анализа</li>
                <li><strong>Удаленный мониторинг</strong>: Сбор данных с автономных датчиков, работающих в режиме глубокого сна, и их отправка в облако</li>
            </ul>
        </section>
        
        <section class="card">
            <h2>⚠️ Важные заметки</h2>
            <div class="warning">
                <p><strong>Внимание!</strong> Проект содержит несколько <strong>независимых примеров</strong>. Для создания готового устройства может потребоваться объединение их логики.</p>
            </div>
            <p>• Режим <strong>глубокого сна</strong> прерывает все сетевые подключения (Wi-Fi, BLE). При пробуждении соединения нужно устанавливать заново.</p>
            <p>• Внимательно настройте <strong>политики безопасности AWS IoT</strong>, чтобы разрешить вашему устройству только необходимые действия (publish/subscribe).</p>
        </section>
    </main>
    
    <aside class="sidebar">
        <section class="card">
            <h2>📊 Статус проекта</h2>
            <p>Проект находится на <strong>ранней стадии разработки</strong> (незавершенный прототип)</p>
            
            <div class="project-status">
                <div class="status-item">
                    <div class="status-value">5</div>
                    <div>коммитов</div>
                </div>
                <div class="status-item">
                    <div class="status-value">2</div>
                    <div>языка</div>
                </div>
                <div class="status-item">
                    <div class="status-value">0</div>
                    <div>релизов</div>
                </div>
            </div>
            
            <p style="margin-top: 15px;"><strong>Последнее обновление:</strong><br>11 января 2024 г.</p>
            <p><strong>Версия:</strong><br>Отсутствует официальный релиз</p>
        </section>
        
        <section class="card">
            <h2>🔗 Ссылки</h2>
            <ul class="file-list">
                <li><a href="https://github.com/igoreshk/esp32-mqtt-aws" target="_blank">Репозиторий проекта</a></li>
                <li><a href="https://aws.amazon.com/ru/iot-core/" target="_blank">AWS IoT Core</a></li>
                <li><a href="https://www.espressif.com/ru/products/socs/esp32" target="_blank">ESP32 информация</a></li>
                <li><a href="https://docs.aws.amazon.com/iot/latest/developerguide/what-is-aws-iot.html" target="_blank">Документация AWS IoT</a></li>
            </ul>
        </section>
        
        <section class="card">
            <h2>📈 Распределение кода</h2>
            <p><strong>C++</strong> - 70.2%</p>
            <div style="background-color: #e0e0e0; border-radius: 3px; height: 10px; margin: 5px 0 15px;">
                <div style="background-color: #2a5298; width: 70.2%; height: 100%; border-radius: 3px;"></div>
            </div>
            
            <p><strong>Python</strong> - 29.8%</p>
            <div style="background-color: #e0e0e0; border-radius: 3px; height: 10px; margin: 5px 0 15px;">
                <div style="background-color: #3a6bc2; width: 29.8%; height: 100%; border-radius: 3px;"></div>
            </div>
        </section>
    </aside>
</div>

<footer>
    <p>Автор проекта: <a href="https://github.com/igoreshk" target="_blank">igoreshk</a></p>
    <p>Репозиторий: <a href="https://github.com/igoreshk/esp32-mqtt-aws" target="_blank">https://github.com/igoreshk/esp32-mqtt-aws</a></p>
    <p style="margin-top: 10px; font-size: 0.8rem;">Документация создана на основе анализа репозитория</p>
</footer>
