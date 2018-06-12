import xbmcaddon, util, commands

# To install youtube-dl run the following commands:
# sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
# sudo chmod a+rx /usr/local/bin/youtube-dl

channels = {
    '01 TVE1' : 'url: http://www.rtve.es/directo/la-1/',
    '02 TVE2' : 'url: http://www.rtve.es/directo/la-2/',
    '03 Antena3' : 'https://atresplayerp-i.akamaized.net/antena3mpp/master.m3u8',
    '04 Cuatro' : 'http://mdsiosgeo2-lh.akamaihd.net/i/mitele/esmediaset_22@168498/index_0_av-b.m3u8',
    '05 Cinco' : 'http://mdsios1-lh.akamaihd.net/i/mitele/esmediaset_11@168471/index_0_av-b.m3u8',
    '06 La Sexta' : 'http://a3live-lh.akamaihd.net/i/lasexta_1@35272/master.m3u8',
    '07 24H' : 'url: http://www.rtve.es/directo/canal-24h/',
    '08 TDP' : 'url: http://www.rtve.es/directo/teledeporte/',
    '09 Cataluna' : 'http://rtve-live.hds.adaptive.level3.net/hls-live/rtvegl7-la1calv3aomgl7/_definst_/live.m3u8',
}


def playVideo(params):
    #util.notify('plugin.video.mytv', "playing video %r" % params['channel'])
    addon = xbmcaddon.Addon('plugin.video.mytv')
    channel = channels[params['channel']]
    if channel.startswith('url:'):
        channel = channel.split()[-1]
        channel = commands.getoutput('youtube-dl -g %s' % channel).split()[-1]
    util.playMedia(addon.getAddonInfo('name'), addon.getAddonInfo('icon'), channel )

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
