from UnityFont import UnityFont

font = UnityFont("24.dat");
font.character_spacing = 2;
font.test();
font.convert_to_raw("24.nw.dat", "C:/Windows/Fonts/SourceHanSansSC-Bold.otf");