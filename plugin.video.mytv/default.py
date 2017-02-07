import xbmcaddon, util

channels = {
    '01 TVE1' : 'http://rtve-live.hds.adaptive.level3.net/hls-live/rtvegl7-la1lv3aomgl7/_definst_/live.m3u8',
    '02 TVE2' : 'http://rtve-live.hds.adaptive.level3.net/hls-live/rtvegl0-la2lv3aomgl0/_definst_/live.m3u8',
    '03 Antena3' : 'http://a3live-lh.akamaihd.net/i/antena3_1@35248/index_1_av-p.m3u8',
    '04 Cuatro' : 'http://mdsiosgeo2-lh.akamaihd.net/i/mitele/esmediaset_22@168498/index_0_av-b.m3u8',
    '05 Cinco' : 'http://mdsios1-lh.akamaihd.net/i/mitele/esmediaset_11@168471/index_0_av-b.m3u8',
    '06 La Sexta' : 'http://a3live-lh.akamaihd.net/i/lasexta_1@35272/master.m3u8',
    '07 24H' : 'http://rtve-live.hds.adaptive.level3.net/hls-live/rtvegl8-24hlv3aomgl8/_definst_/live.m3u8',
    '08 TDP' : 'http://hlsackdn_gl8-lh.akamaihd.net/i/hlslive_1@441481/master.m3u8',
    '09 Cataluna' : 'http://rtve-live.hds.adaptive.level3.net/hls-live/rtvegl7-la1calv3aomgl7/_definst_/live.m3u8',
    '10 Test' : 'http://hlsackdn_gl7-lh.akamaihd.net/i/hlslive_1@439315/master.m3u8',

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
