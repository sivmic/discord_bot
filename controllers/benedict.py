import controllers.controller as controller
import random


class Benedict(controller.Controller):
    async def process(self, params, message, client):
        first_name_list = ["Bumblebee", "Bandersnatch", "Broccoli", "Rinkydink", "Bombadil", "Boilerdang", "Bandicoot",
                           "Fragglerock", "Muffintop", "Congleton", "Blubberdick", "Buffalo", "Benadryl", "Butterfree",
                           "Burberry", "Whippersnatch", "Buttermilk", "Beezlebub", "Budapest", "Boilerdang",
                           "Blubberwhale", "Bumberstump", "Bulbasaur", "Cogglesnatch", "Liverswort", "Bodybuild",
                           "Johnnycash", "Bendydick", "Burgerking", "Bonaparte", "Bunsenburner", "Billiardball",
                           "Bukkake", "Baseballmitt", "Blubberbutt", "Baseballbat", "Rumblesack", "Barister",
                           "Danglerack", "Rinkydink", "Bombadil", "Honkytonk", "Billyray", "Bumbleshack", "Snorkeldink",
                           "Anglerfish", "Beetlejuice", "Bedlington", "Bandicoot", "Boobytrap", "Blenderdick",
                           "Bentobox",
                           "Anallube", "Pallettown", "Wimbledon", "Buttercup", "Blasphemy", "Syphilis", "Snorkeldink",
                           "Brandenburg", "Barbituate", "Snozzlebert", "Tiddleywomp", "Bouillabaisse", "Wellington",
                           "Benetton", "Bendandsnap", "Timothy", "Brewery", "Bentobox", "Brandybuck", "Benjamin",
                           "Buckminster", "Bourgeoisie", "Bakery", "Oscarbait", "Buckyball", "Bourgeoisie",
                           "Burlington",
                           "Buckingham", "Barnoldswick"]

        last_name_list = ["Coddleswort", "Crumplesack", "Curdlesnoot", "Calldispatch", "Humperdinck", "Rivendell",
                          "Cuttlefish", "Lingerie", "Vegemite", "Ampersand", "Cumberbund", "Candycrush", "Clombyclomp",
                          "Cragglethatch", "Nottinghill", "Cabbagepatch", "Camouflage", "Creamsicle", "Curdlemilk",
                          "Upperclass", "Frumblesnatch", "Crumplehorn", "Talisman", "Candlestick", "Chesterfield",
                          "Bumbersplat", "Scratchnsniff", "Snugglesnatch", "Charizard", "Carrotstick", "Cumbercooch",
                          "Crackerjack", "Crucifix", "Cuckatoo", "Cockletit", "Collywog", "Capncrunch", "Covergirl",
                          "Cumbersnatch", "Countryside", "Coggleswort", "Splishnsplash", "Copperwire", "Animorph",
                          "Curdledmilk", "Cheddarcheese", "Cottagecheese", "Crumplehorn", "Snickersbar", "Banglesnatch",
                          "Stinkyrash", "Cameltoe", "Chickenbroth", "Concubine", "Candygram", "Moldyspore",
                          "Chuckecheese", "Cankersore", "Crimpysnitch", "Wafflesmack", "Chowderpants", "Toodlesnoot",
                          "Clavichord", "Cuckooclock", "Oxfordshire", "Cumbersome", "Chickenstrips", "Battleship",
                          "Commonwealth", "Cunningsnatch", "Custardbath", "Kryptonite", "Curdlesnoot", "Cummerbund",
                          "Coochyrash", "Crackerdong", "Crackerdong", "Curdledong", "Crackersprout", "Crumplebutt",
                          "Colonist", "Coochierash"]

        full_name_list = ["Wimbledon Tennismatch", "Rinkydink Curdlesnoot", "Butawhiteboy Cantbekhan",
                          "Benadryl Claritin", "Bombadil Rivendell", "Wanda's Crotchfruit", "Wanda's Crotchfruit",
                          "Biblical Concubine", "Butawhiteboy Cantbekhan", "Syphilis Cankersore",
                          "Butawhiteboy Cantbekhan", "Benedict Timothy Carlton Cumberbatch", "Wanda's Son",
                          "Buckminster Fullerene", "Bourgeoisie Capitalist"]

        if random.randint(0, 4) == 0:
            name = full_name_list[random.randint(0, len(full_name_list) - 1)]
        else:
            name = first_name_list[random.randint(0, len(first_name_list) - 1)] + " " + last_name_list[
                random.randint(0, len(last_name_list) - 1)]

        await client.send_message(message.channel, name)
