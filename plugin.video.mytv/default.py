import xbmcaddon, util, commands

channels = {
    '01 TVE1' : commands.getoutput('youtube-dl -g http://www.rtve.es/directo/la-1/').split()[-1],
    '02 TVE2' : commands.getoutput('youtube-dl -g http://www.rtve.es/directo/la-2/').split()[-1],
    '03 Antena3' : 'http://a3live-lh.akamaihd.net/i/antena3_1@35248/index_1_av-p.m3u8',
    '04 Cuatro' : 'http://mdsiosgeo2-lh.akamaihd.net/i/mitele/esmediaset_22@168498/index_0_av-b.m3u8',
    '05 Cinco' : 'http://mdsios1-lh.akamaihd.net/i/mitele/esmediaset_11@168471/index_0_av-b.m3u8',
    '06 La Sexta' : 'http://a3live-lh.akamaihd.net/i/lasexta_1@35272/master.m3u8',
    '07 24H' : commands.getoutput('youtube-dl -g http://www.rtve.es/directo/canal-24h/').split()[-1],
    '08 TDP' : commands.getoutput('youtube-dl -g http://www.rtve.es/directo/teledeporte/').split()[-1],
    '09 Cataluna' : 'http://rtve-live.hds.adaptive.level3.net/hls-live/rtvegl7-la1calv3aomgl7/_definst_/live.m3u8',
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
