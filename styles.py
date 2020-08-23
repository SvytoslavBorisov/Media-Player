framePlayer = '''QFrame{
                    background-color: qlineargradient(spread:reflect, x1:0.528, y1:0.971591, x2:0.528955, y2:0.506, 
                                      stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));
                    border-radius: 15px; 
                    border: 1px solid black;}'''

frameTitle = '''QFrame{
                    background-color: qlineargradient(spread:reflect, x1:0.54, y1:0.471591, x2:0.54, y2:1, 
                                      stop:0 rgba(222, 142, 55, 255), stop:1 rgba(240, 200, 100, 255));
                    border-radius: 15px;
                    border: 1px solid black;}'''

bRadioState = '''QPushButton{
                    border-radius: 15px;
                    border: 1px solid gray;
                    image: url(Images/radio_notactive1.png);}
                QPushButton:hover{
                    border-radius: 15px;
                    border: 1px solid black;
                    image: url(Images/radio_notactive1.png);}
                QPushButton:checked{
                    border-radius: 15px;
                    border: 1px solid gray;
                    image: url(Images/radio_active.png);}'''

bAudioState = '''QPushButton{
                    border-radius: 15px;
                    border: 1px solid gray;
                    image: url(Images/audio_notactive1.png);}
                QPushButton:hover{
                    border-radius: 15px;
                    border: 1px solid black;
                    image: url(Images/audio_notactive1.png);}
                QPushButton:checked{
                    border-radius: 15px;
                    border: 1px solid gray;
                    image: url(Images/audio_active.png);}'''

bVideoState = '''QPushButton{
                    border-radius: 15px;
                    border: 1px solid gray;
                    image: url(Images/video_notactive1.png);}
                QPushButton:hover{
                    border-radius: 15px;
                    border: 1px solid black;
                    image: url(Images/video_notactive1.png);}
                QPushButton:checked{
                    border-radius: 15px;
                    border: 1px solid gray;
                    image: url(:/img/Images/video_active.png);}'''

lArtist = ''' border: 0px;
              background-color: none;'''

lTitle = ''' border: 0px;
              background-color: none;'''

hsMusicSlider = ''' QSlider {
                        border: 0px;
                        background: none;}
                    QSlider::groove:horizontal {
                        border: 1px solid #bbb;
                        background: white;
                        height: 10px;}
                    QSlider::sub-page:horizontal {
                        background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,  stop: 0 #66e, stop: 1 #FC0B0B);
                        background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,  stop: 0 #FC0B0B, stop: 1 #F5ED14);
                        border: 1px solid #777;height: 14px;}
                    QSlider::add-page:horizontal {
                        background: black;
                        border: 1px solid #777;
                        height: 14px;}
                    QSlider::handle:horizontal {
                        background: none;
                        width: 12px;
                        margin-top: -6px;
                        margin-bottom: -6px;
                        border-radius: 7px;}
                    QSlider::handle:horizontal:hover {
                        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #fff, stop:1 #ddd);
                        border: 1px solid #444;
                        border-radius: 7px;}
                    QSlider::sub-page:horizontal:disabled {
                        background: #bbb;
                        border-color: #999;}
                    QSlider::add-page:horizontal:disabled {
                        background: #eee;
                        border-color: #999;}
                    QSlider::handle:horizontal:disabled {
                        background: #eee;
                        border: 1px solid #aaa;
                        border-radius: 4px;}'''

pbPrevious = '''QPushButton{
                    border-radius: 5px;
                    image: url(:/img/Images/skip-previous.png);
                    background-color: none;}
                QPushButton:hover{
                    border-radius: 5px;
                    border: 1px solid gray;
                    image: url(:/img/Images/skip-previous.png);}
                QPushButton:pressed{
                    border-radius: 5px;
                    image: url(:/img/Images/skip-previous-orange.png);}'''

pbInBegin = ''' QPushButton{
                    border-radius: 5px;
                    image: url(:/img/Images/stop.png);
                    background-color: none;}
                QPushButton:hover{
                    border-radius: 5px;
                    border: 1px solid gray;
                    image: url(:/img/Images/stop.png);}
                QPushButton:checked{
                    border-radius: 5px;
                    image: url(:/img/Images/stop-orange.png);}'''

pbPlay = '''QPushButton{
                border-radius: 5px;
                image: url(:/img/Images/play.png);
                background-color: none;}
            QPushButton:hover{
                border-radius: 5px;
                border: 1px solid gray;
                image: url(:/img/Images/play.png);}
            QPushButton:checked{
                border-radius: 5px;
                image: url(:/img/Images/play-orange.png);}'''

pbStop = '''QPushButton{
                border-radius: 5px;
                image: url(:/img/Images/pause.png);
                background-color: none;}
            QPushButton:hover{
                border-radius: 5px;
                border: 1px solid gray;
                image: url(:/img/Images/pause.png);}
            QPushButton:checked{
                border-radius: 5px;
                image: url(:/img/Images/pause-orange.png);}'''

pbNext = '''QPushButton{
                border-radius: 5px;
                image: url(:/img/Images/skip-next.png);
                background-color: none;}
            QPushButton:hover{
                border-radius: 5px;
                border: 1px solid gray;
                image: url(:/img/Images/skip-next.png);}
            QPushButton:pressed{
                border-radius: 5px;
                image: url(:/img/Images/skip-next-orange.png);}'''

pbVolume = '''  QPushButton{
                    border-radius: 5px;
                    image: url(:/img/Images/volume.png);
                    background-color: none;}
                QPushButton:hover{
                    border-radius: 5px;
                    border: 1px solid gray;
                    image: url(:/img/Images/volume.png);}
                QPushButton:checked{
                    border-radius: 5px;
                    image: url(:/img/Images/volume-orange.png);}'''

hsVolumeSlider = '''QSlider {
                        border: 0px;
                        background: none;}
                    QSlider::groove:horizontal {
                        border: 1px solid #bbb;
                        background: white;
                        height: 3px;
                        border-radius: 4px;}
                    QSlider::sub-page:horizontal {
                        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,  stop: 0 #66e, stop: 1 #FC0B0B);
                        background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,  stop: 0 #FC0B0B, stop: 1 #F5ED14);
                        border: 1px solid #777;
                        height: 14px;
                        border-radius: 4px;}
                    QSlider::add-page:horizontal {
                        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,  stop: 0 #000, stop: 1 #FC0B0B);
                        background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,  stop: 0 #892919, stop: 1 #000);
                        border: 1px solid #777;
                        height: 14px;
                        border-radius: 4px;}
                    QSlider::handle:horizontal {
                        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #eee, stop:1 #ccc);
                        border: 1px solid #777;
                        width: 12px;
                        margin-top: -6px;
                        margin-bottom: -6px;
                        border-radius: 7px;}
                    QSlider::handle:horizontal:hover {
                        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,stop:0 #fff, stop:1 #ddd);
                        border: 1px solid #444;
                        border-radius: 7px;};
                    QSlider::sub-page:horizontal:disabled {
                        background: #bbb;
                        border-color: #999;}
                    QSlider::add-page:horizontal:disabled {
                        background: #eee;
                        border-color: #999;}
                    QSlider::handle:horizontal:disabled {
                        background: #eee;
                        border: 1px solid #aaa;
                        border-radius: 4px;};'''

playlistMenu = '''  QMenu {
                        background-color: rgb(222, 142, 55);
                        border: 3px solid rgb(0, 0, 0);;
                        color: rgb(0, 0, 0);}
                    QMenu::separator {
                        height: 2px;
                        margin-left: 10px;
                        margin-right: 5px;
                        background-color: rgb(0, 0, 0);}'''

wWWS = "QWidget { "
"background-color: #454545; "
"border: 1px solid black; "
"}"

wLSS = "QLabel { "
"color: #8f8f8f; "
"border: none; "
"margin: 6px; "
"}"

wCSS = "QToolButton { "
"image: url(:/buttons/close-orange.png);"
"background-color: #292929; "
"icon-size: 12px;"
"padding-left: 10px;"
"padding-right: 10px;"
"padding-top: 5px;"
"padding-bottom: 5px;"
"border: 1px solid #292929; "
"}"
"QToolButton:hover {"
"image: url(:/buttons/close.png); "
"}"
"QToolButton:pressed { "
"image: url(:/buttons/close.png);"
"background-color: #de8e37; "
"}"

wMMS = "QToolButton { "
"image: url(:/buttons/window-maximize-gray.png);"
"background-color: #292929;"
"icon-size: 12px;"
"padding-left: 10px;"
"padding-right: 10px;"
"padding-top: 5px;"
"padding-bottom: 5px;"
"border: 1px solid #292929; "
"}"
"QToolButton:hover {"
"image: url(:/buttons/window-maximize.png); "
"}"
"QToolButton:pressed { "
"image: url(:/buttons/window-maximize.png);"
"background-color: #de8e37; "
"}"

wRSS = "QToolButton { "
"image: url(:/buttons/window-restore-gray.png);"
"background-color: #292929;"
"icon-size: 12px;"
"padding-left: 10px;"
"padding-right: 10px;"
"padding-top: 5px;"
"padding-bottom: 5px;"
"border: 1px solid #292929; "
"}"
"QToolButton:hover {"
"image: url(:/buttons/window-restore.png); "
"}"
"QToolButton:pressed { "
"image: url(:/buttons/window-restore.png);"
"background-color: #de8e37; "
"}"
