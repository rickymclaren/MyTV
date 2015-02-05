import xbmcaddon, util

channels = {

    'TVE1 rtmp' : 'rtmp://rtvefs.fplive.net:1935/rtve-live-live?ovpfv=2.1.2 playpath=RTVE_LA1_LV3_WEB_NOG swfUrl=http://swf.rtve.es/swf/4.2.26/RTVEPlayerVideo.swf pageUrl=http://www.rtve.es/noticias/directo-la-1/ swfVfy=true live=true timeout=10',
    'TVE1 iOS' : 'http://iphonelive.rtve.es/LA1_LV3_IPH/LA1_LV3_IPH.m3u8',
    'TVE2 iOS' : 'http://iphonelive.rtve.es/LA2_LV3_IPH/LA2_LV3_IPH.m3u8',
    'Teledeporte iOS' : 'http://iphonelive.rtve.es/TDP_LV3_IPH/TDP_LV3_IPH.m3u8',
    'Canal 24H iOS' : 'http://iphonelive.rtve.es/24H_LV3_IPH/24H_LV3_IPH.m3u8',
    'Antena3' : 'rtmp://antena3fms35livefs.fplive.net/antena3fms35live-live/ playpath=stream-antena3_1 swfUrl=http://player.longtailvideo.com/player.swf live=1 pageUrl=http://www.omegateam.byethost7.com/ch/i-antena-3.php --live',
    'La Sexta' : 'rtmp://antena3fms35livefs.fplive.net/antena3fms35live-live/ playpath=stream-lasexta_1 swfUrl=http://player.longtailvideo.com/player.swf live=1 pageUrl=http://biophobia.es/?p=343'

}


def playVideo(params):
    #util.notify('plugin.video.mytv', "playing video %r" % params['channel'])
    addon = xbmcaddon.Addon('plugin.video.mytv')
    util.playMedia(addon.getAddonInfo('name'), addon.getAddonInfo('icon'), channels[params['channel']] )

def buildMenu():
    for channel in sorted(channels.keys()):
        params = {'play':1}
        params['channel'] = channel
        link = util.makeLink(params)
        util.addMenuItem(channel, link, 'DefaultVideo.png', 'DefaultVideo.png')
    util.endListing()

parameters = util.parseParameters()
if 'play' in parameters:
    playVideo(parameters)
else:
    buildMenu()

