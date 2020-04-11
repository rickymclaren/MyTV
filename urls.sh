#! /usr/bin/env bash

echo '#EXTINF:-1,LA-1'
youtube-dl -g http://www.rtve.es/directo/la-1/
echo '#EXTINF:-1,LA-2'
youtube-dl -g http://www.rtve.es/directo/la-2/
echo '#EXTINF:-1,Teledeporte'
youtube-dl -g http://www.rtve.es/directo/teledeporte/
echo '#EXTINF:-1,Canal 24H'
youtube-dl -g http://www.rtve.es/directo/canal-24h/


