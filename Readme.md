# DJI Osmo Pocket File Renamer

![Made by Ukrainian](https://img.shields.io/static/v1?label=Made%20by&message=Ukrainian&labelColor=1f5fb2&color=fad247&style=for-the-badge)

Lately, I was frustrated again by the fact that, when importing files from Osmo Pocket to my phone with DJI Mimo app, the latter one not only gives my photos and videos some strange names like `org_video_6554110_1567420736000.mp4`, but also sets incorrect modification date. So, if you mix within single folder your Osmo Pocket's media and the photos and videos shot by your phone, you'll end up having a completely incorrect sorting order (non-chronological).

The script is intended to fix the problem! :)
It scans the specified folder recursively, renames the files, and updates the modification date, so that `org_video_6554110_1567420736000.mp4` becomes `20190902_123856.mp4` (which stands for _2019-09-02 12:38:56_).

## Pre-requisites
Simply run `pipenv` and it will download all the dependencies
```
> pipenv install
```

## Usage
```
> pipenv run python3 osmo-renamer.py <path-to-your-folder>
```
