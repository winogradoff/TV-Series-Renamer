# TV-Series-Renamer

Rename TV series files. Useful for services like Plex.

Usage:
```
python3 tv-series-renamer.py <directory with tv series>
```

Example:
```
$ ls
Young.Sheldon.2019.S03E01.Quirky.Eggheads.and.Texas.Snow.Globes.1080p.AMZN.WEB-DL.DD5.1.x264-NTb_EniaHD.mkv
Young.Sheldon.2019.S03E02.A.Broom.Closet.and.Satans.Monopoly.Board.1080p.AMZN.WEB-DL.DD5.1.x264-NTb_EniaHD.mkv
Young.Sheldon.2019.S03E03.An.Entrepreneurialist.and.a.Swat.on.the.Bottom.1080p.AMZN.WEB-DL.DD5.1.x264-NTb_EniaHD.mkv
Young.Sheldon.2019.S03E04.Hobbitses.Physicses.and.a.Ball.with.Zip.1080p.AMZN.WEB-DL.DD5.1.x264-NTb_EniaHD.mkv
Young.Sheldon.2019.S03E05.A.Pineapple.and.the.Bosom.of.Male.Friendship.1080p.AMZN.WEB-DL.DD5.1.x264-NTb_EniaHD.mkv
Young.Sheldon.2019.S03E06.A.Parasol.and.a.Hell.of.an.Arm.1080p.AMZN.WEB-DL.DD5.1.x264-NTb_EniaHD.mkv
Young.Sheldon.2019.S03E07.Pongo.Pygmaeus.and.a.Culture.that.Encourages.Spitting.1080p.AMZN.WEB-DL.DD5.1.x264-NTb_EniaHD.mkv
Young.Sheldon.2019.S03E08.The.Sin.of.Greed.and.a.Chimichanga.from.Chi-Chis.1080p.AMZN.WEB-DL.DD5.1.x264-NTb_EniaHD.mkv
Young.Sheldon.2019.S03E09.A.Party.Invitation.Football.Grapes.and.an.Earth.Chicken.1080p.AMZN.WEB-DL.DD5.1.x264-NTb_EniaHD.mkv

$ python3 tv-series-renamer.py .

Looking for files in a directory...
Enter prefix (empty for "Young Sheldon 2019"): Young Sheldon
Rename suggestions:
Young.Sheldon.2019.S03E01.Quirky.Eggheads.and.Texas.Snow.Globes.1080p.AMZN.WEB-DL.DD5.1.x264-NTb_EniaHD.mkv -> Young Sheldon s03e01.mkv
Young.Sheldon.2019.S03E02.A.Broom.Closet.and.Satans.Monopoly.Board.1080p.AMZN.WEB-DL.DD5.1.x264-NTb_EniaHD.mkv -> Young Sheldon s03e02.mkv
Young.Sheldon.2019.S03E03.An.Entrepreneurialist.and.a.Swat.on.the.Bottom.1080p.AMZN.WEB-DL.DD5.1.x264-NTb_EniaHD.mkv -> Young Sheldon s03e03.mkv
Young.Sheldon.2019.S03E04.Hobbitses.Physicses.and.a.Ball.with.Zip.1080p.AMZN.WEB-DL.DD5.1.x264-NTb_EniaHD.mkv -> Young Sheldon s03e04.mkv
Young.Sheldon.2019.S03E05.A.Pineapple.and.the.Bosom.of.Male.Friendship.1080p.AMZN.WEB-DL.DD5.1.x264-NTb_EniaHD.mkv -> Young Sheldon s03e05.mkv
Young.Sheldon.2019.S03E06.A.Parasol.and.a.Hell.of.an.Arm.1080p.AMZN.WEB-DL.DD5.1.x264-NTb_EniaHD.mkv -> Young Sheldon s03e06.mkv
Young.Sheldon.2019.S03E07.Pongo.Pygmaeus.and.a.Culture.that.Encourages.Spitting.1080p.AMZN.WEB-DL.DD5.1.x264-NTb_EniaHD.mkv -> Young Sheldon s03e07.mkv
Young.Sheldon.2019.S03E08.The.Sin.of.Greed.and.a.Chimichanga.from.Chi-Chis.1080p.AMZN.WEB-DL.DD5.1.x264-NTb_EniaHD.mkv -> Young Sheldon s03e08.mkv
Young.Sheldon.2019.S03E09.A.Party.Invitation.Football.Grapes.and.an.Earth.Chicken.1080p.AMZN.WEB-DL.DD5.1.x264-NTb_EniaHD.mkv -> Young Sheldon s03e09.mkv
Press y for continue: y
Renaming...
Done!

$ ls
Young Sheldon s03e01.mkv	Young Sheldon s03e03.mkv	Young Sheldon s03e05.mkv
Young Sheldon s03e07.mkv	Young Sheldon s03e09.mkv	Young Sheldon s03e02.mkv
Young Sheldon s03e04.mkv	Young Sheldon s03e06.mkv	Young Sheldon s03e08.mkv
```
