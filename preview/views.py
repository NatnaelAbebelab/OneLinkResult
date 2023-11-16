from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.http import JsonResponse
import pymongo, time, uuid, datetime, requests, os
# Create your views here.

def index (request) :
    return render (request,'404.html')

def result (request, sublink) :
    client = pymongo.MongoClient("mongodb+srv://natnaelabebelab:04FepwvUgcQOFqIx@socialmedialinks.zyvulmy.mongodb.net/?retryWrites=true&w=majority")
    # Database Name
    db = client["Links"]
    # Collection Name
    col = db["LinksCollection"]

    record = col.find_one({'sub_link': sublink.lower()})
    if record is None :
        return render(request, '404.html')
    
    # check single or multiple
    if record.get('type') == 'multiple' :
        # get every attribute
        facebook, instagram, twitter, telegram, whatsapp, youtube, pinterest, tiktok, google, website, phone, email, location, custom_link = '' , '', '', '' , '', '', '', '', '', '', '', '', '',''
        facebooks, instagrams, twitters, telegrams, whatsapps, youtubes, pinterests, tiktoks, googles, websites, phones, emails, locations, custom_links = [], [], [], [], [], [], [], [], [], [], [], [], [], []
        facebooks_text, instagrams_text, twitters_text, telegrams_text, whatsapps_text, youtubes_text, pinterests_text, tiktoks_text, googles_text, websites_text, phones_text, emails_text, locations_text, custom_links_text = [], [], [], [], [], [], [], [], [], [], [], [], [], []

        if '-' in record.get('facebook') :
            facebook = '#'
            facebooks = str(record.get('facebook')).split('-')
            facebooks_text = str(record.get('facebooks_text')).split('-')

        if '-' not in record.get('facebook') :
            facebook = record.get('facebook')
        
        if '-' in record.get('instagram') :
            instagram = '#'
            instagrams = str(record.get('instagram')).split('-')
            instagrams_text = str(record.get('instagrams_text')).split('-')

        if '-' not in record.get('instagram') :
            instagram = record.get('instagram')
        
        if '-' in record.get('twitter') :
            twitter = '#'
            twitters = str(record.get('twitter')).split('-')
            twitters_text = str(record.get('twitters_text')).split('-')

        if '-' not in record.get('twitter') :
            twitter = record.get('twitter')
        
        if '-' in record.get('telegram') :
            telegram = '#'
            telegrams = str(record.get('telegram')).split('-')
            telegrams_text = str(record.get('telegrams_text')).split('-')

        if '-' not in record.get('telegram') :
            telegram = record.get('telegram')
        
        if '-' in record.get('whatsapp') :
            whatsapp = '#'
            whatsapps = str(record.get('whatsapp')).split('-')
            whatsapps_text = str(record.get('whatsapps_text')).split('-')

        if '-' not in record.get('whatsapp') :
            whatsapp = 'https://wa.me/'+ record.get('whatsapp')
        
        if '-' in record.get('youtube') :
            youtube = '#'
            youtubes = str(record.get('youtube')).split('-')
            youtubes_text = str(record.get('youtubes_text')).split('-')

        if '-' not in record.get('youtube') :
            youtube = record.get('youtube')
        
        if '-' in record.get('pinterest') :
            pinterest = '#'
            pinterests = str(record.get('pinterest')).split('-')
            pinterests_text = str(record.get('pinterests_text')).split('-')

        if '-' not in record.get('pinterest') :
            pinterest = record.get('pinterest')
        
        if '-' in record.get('tiktok') :
            tiktok = '#'
            tiktoks = str(record.get('tiktok')).split('-')
            tiktoks_text = str(record.get('tiktoks_text')).split('-')

        if '-' not in record.get('tiktok') :
            tiktok = record.get('tiktok')
        
        if '-' in record.get('google') :
            google = '#'
            googles = str(record.get('google')).split('-')
            googles_text = str(record.get('googles_text')).split('-')

        if '-' not in record.get('google') :
            google = record.get('google')
        
        if '-' in record.get('website') :
            website = '#'
            websites = str(record.get('website')).split('-')
            websites_text = str(record.get('websites_text')).split('-')

        if '-' not in record.get('website') :
            website = record.get('website')
        
        if '-' in record.get('phone') :
            phone = '#'
            phones = str(record.get('phone')).split('-')
            phones_text = str(record.get('phones_text')).split('-')

        if '-' not in record.get('phone') :
            phone = 'tel:' + record.get('phone')
        
        if '-' in record.get('email') :
            email = '#'
            emails = str(record.get('email')).split('-')
            emails_text = str(record.get('emails_text')).split('-')

        if '-' not in record.get('email') :
            email = 'mailto:' + record.get('email')
        
        if '-' in record.get('location') :
            location = '#'
            locations = str(record.get('location')).split('-')
            locations_text = str(record.get('locations_text')).split('-')

        if '-' not in record.get('location') :
            location = record.get('location')
        
        if '-' in record.get('custom_link') :
            custom_link = '#'
            custom_links = str(record.get('custom_link')).split('-')
            custom_links_text = str(record.get('custom_links_text')).split('-')

        if '-' not in record.get('custom_link') :
            custom_link = record.get('custom_link')
        
        # check wheather the backgroud is image or color
        if record.get('background_type') == 'image' :
            #get the background
                return render(request, 'bgtemplate.html', {
                    'sublink' : record.get('sub_link'),
                    'name' : record.get('name'),
                    'logo' : record.get('logo'),
                    'desc' : record.get('desc'),
                    'facebook' : facebook,
                    'facebook_val' : zip(facebooks,facebooks_text),
                    'instagram' : instagram,
                    'instagram_val' : zip(instagrams,instagrams_text),
                    'twitter' : twitter,
                    'twitter_val' : zip(twitters,twitters_text),
                    'telegram' : telegram,
                    'telegram_val' : zip(telegrams,telegrams_text),
                    'whatsapp' : whatsapp,
                    'whatsapp_val' : zip(whatsapps,whatsapps_text),
                    'youtube' : youtube,
                    'youtube_val' : zip(youtubes,youtubes_text),
                    'pinterest' : pinterest,
                    'pinterest_val' : zip(pinterests,pinterests_text),
                    'tiktok' : tiktok,
                    'tiktok_num' : zip(tiktoks,tiktoks_text),
                    'google' : google,
                    'googleText' : record.get('google_text'),
                    'google_val' : zip(googles,googles_text),
                    'website' : website,
                    'websiteText' : record.get('web_text'),
                    'website_val' : zip(websites,websites_text),
                    'phone' : phone,
                    'phoneText' : record.get('phone_text'),
                    'phone_val' : zip(phones,phones_text),
                    'email' : email,
                    'emailText' : record.get('email_text'),
                    'email_val' : zip(emails,emails_text),
                    'location' : location,
                    'locText' : record.get('loc_text'),
                    'location_val' : zip(locations,locations_text),
                    'customlink' : custom_link,
                    'customlinkText' : record.get('custom_link_text'),
                    'custom_link_val' : zip(custom_links,custom_links_text),
                    'backgroundImage' : record.get('background_image'),
                    'fontColor' : record.get('font_color')
                })

        if record.get('background_type') == 'color' :
            #get the logo only
                return render(request, 'colortemplate.html', {
                    'sublink' : record.get('sub_link'),
                    'name' : record.get('name'),
                    'logo' : record.get('logo'),
                    'desc' : record.get('desc'),
                    'facebook' : facebook,
                    'facebook_val' : zip(facebooks,facebooks_text),
                    'instagram' : instagram,
                    'instagram_val' : zip(instagrams,instagrams_text),
                    'twitter' : twitter,
                    'twitter_val' : zip(twitters,twitters_text),
                    'telegram' : telegram,
                    'telegram_val' : zip(telegrams,telegrams_text),
                    'whatsapp' : whatsapp,
                    'whatsapp_val' : zip(whatsapps,whatsapps_text),
                    'youtube' : youtube,
                    'youtube_val' : zip(youtubes,youtubes_text),
                    'pinterest' : pinterest,
                    'pinterest_val' : zip(pinterests,pinterests_text),
                    'tiktok' : tiktok,
                    'tiktok_num' : zip(tiktoks,tiktoks_text),
                    'google' : google,
                    'googleText' : record.get('google_text'),
                    'google_val' : zip(googles,googles_text),
                    'website' : website,
                    'websiteText' : record.get('web_text'),
                    'website_val' : zip(websites,websites_text),
                    'phone' : phone,
                    'phoneText' : record.get('phone_text'),
                    'phone_val' : zip(phones,phones_text),
                    'email' : email,
                    'emailText' : record.get('email_text'),
                    'email_val' : zip(emails,emails_text),
                    'location' : location,
                    'locText' : record.get('loc_text'),
                    'location_val' : zip(locations,locations_text),
                    'customlink' : custom_link,
                    'customlinkText' : record.get('custom_link_text'),
                    'custom_link_val' : zip(custom_links,custom_links_text),
                    'backgroundColor' : record.get('background_color'),
                    'fontColor' : record.get('font_color')
                })

    if record.get('type') == 'single' :
        # check wheather the backgroud is image or color
        if record.get('background_type') == 'image' :
            #get the background
                return render(request, 'bgtemplate.html', {
                    'sublink' : record.get('sub_link'),
                    'name' : record.get('name'),
                    'logo' : record.get('logo'),
                    'desc' : record.get('desc'),
                    'facebook' : record.get('facebook'),
                    'instagram' : record.get('instagram'),
                    'twitter' : record.get('twitter'),
                    'telegram' : record.get('telegram'),
                    'whatsapp' : 'https://wa.me/' + record.get('whatsapp'),
                    'youtube' : record.get('youtube'),
                    'pinterest' : record.get('pinterest'),
                    'tiktok' : record.get('tiktok'),
                    'google' : record.get('google'),
                    'googleText' : record.get('google_text'),
                    'website' : record.get('website'),
                    'websiteText' : record.get('web_text'),
                    'phone' : 'tel:' + record.get('phone'),
                    'phoneText' : record.get('phone_text'),
                    'email' : 'mailto:' + record.get('email'),
                    'emailText' : record.get('email_text'),
                    'location' : record.get('location'),
                    'locText' : record.get('loc_text'),
                    'customlink' : record.get('custom_link'),
                    'customlinkText' : record.get('custom_link_text'),
                    'backgroundImage' : record.get('background_image'),
                    'fontColor' : record.get('font_color')
                })

        else :
            #get the logo only
                return render(request, 'colortemplate.html', {
                    'sublink' : record.get('sub_link'),
                    'name' : record.get('name'),
                    'logo' :record.get('logo'),
                    'desc' : record.get('desc'),
                    'facebook' : record.get('facebook'),
                    'instagram' : record.get('instagram'),
                    'twitter' : record.get('twitter'),
                    'telegram' : record.get('telegram'),
                    'whatsapp' : 'https://wa.me/' + record.get('whatsapp'),
                    'youtube' : record.get('youtube'),
                    'pinterest' : record.get('pinterest'),
                    'tiktok' : record.get('tiktok'),
                    'google' : record.get('google'),
                    'googleText' : record.get('google_text'),
                    'website' : record.get('website'),
                    'websiteText' : record.get('web_text'),
                    'phone' : 'tel:' + record.get('phone'),
                    'phoneText' : record.get('phone_text'),
                    'email' : 'mailto:' + record.get('email'),
                    'emailText' : record.get('email_text'),
                    'location' : record.get('location'),
                    'locText' : record.get('loc_text'),
                    'customlink' : record.get('custom_link'),
                    'customlinkText' : record.get('custom_link_text'),
                    'backgroundColor' : record.get('background_color'),
                    'fontColor' : record.get('font_color')
                })
    
    return render(request, '404.html') 