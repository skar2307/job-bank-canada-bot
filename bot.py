import hikari
import lightbulb
import scrape

bot = lightbulb.BotApp(
    token = "OTM4ODA5OTQ4MDQ4MDgwOTk3.Yfvs5Q.X8IqsUlDVn-r0KDx6YdIaR5nH-4", 
    default_enabled_guilds=(725073889708998757)
)

@bot.command
@lightbulb.option('position', 'keyword related to the desired job.')
@lightbulb.option('location', 'city of the job')
@lightbulb.command('jobs', 'Pulls a list of job postings')
@lightbulb.implements(lightbulb.SlashCommand)
async def jobs(ctx):

    position = ctx.options.position
    location = ctx.options.location

    scrape.getJobs(position, location)

    embed = hikari.Embed()
    embed.add_field('Title', scrape.jobList[0]['title'])
    embed.add_field('Business', scrape.jobList[0]['business'])
    embed.add_field('Location', scrape.jobList[0]['location'])
    embed.add_field('Salary', scrape.jobList[0]['salary'])
    embed.add_field('Date', scrape.jobList[0]['date'])
    embed.set_footer('Please contact SK#6519 if you have any concerns')

    print(scrape.jobList[0]['salary'])

    await ctx.respond(embed=embed)

    scrape.jobList = []

bot.run()