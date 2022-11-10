////////////////////////////////////
////////////////////////////////////
// `index.js` is the core of Astride.
// Most of the bot logic and boilerplate are stored here.
////////////////////////////////////
////////////////////////////////////

// Boilerplate & secret token
const { Client, GatewayIntentBits } = require("discord.js")
const { token } = require("./config.json")
// Create a new client instance and declare our (peacefull) intents
const client = new Client({
  intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMessages,
    GatewayIntentBits.MessageContent,
    GatewayIntentBits.GuildMembers,
  ],
})

// When the client is ready, run this code (only once)
client.once("ready", () => {
  console.log("🕊️ Astride prend son envol")
  // Check mastodon every hour
  update_mastodon_channel()
  setInterval(update_mastodon_channel, 1000 * 60 * 10)
})

//////////////////
// Basics Helpers
//////////////////

/**
 * Send a Discord message on a Discord channel
 * @param {*} channel_id where to send
 * @param {*} payload to send
 */
const send_message_on_channel = (channel_id, payload) => {
  client.channels.cache.get(channel_id).send(payload)
}

//////////////////
// Interactions with slash commands
//////////////////
client.on("interactionCreate", async (interaction) => {
  if (!interaction.isCommand()) return

  const { commandName } = interaction

  switch (commandName) {
    case "question":
      await interaction.reply(
        `Bonjour. Merci de poser votre question en un seul message, dans le salon pertinent, en indiquant clairement votre problème, ce que vous essayez de faire, et en joignant un screen ou un message d'erreur si nécessaire.\n➡️ Voir la règle 1 de <#218748267431854081>`
      )
      break
    case "recrutement":
      await interaction.reply(
        `Bonjour. Pour recruter, votre sérieux et vos connaissances doivent être à la mesure de l'équipe que vous recherchez. Expliquez clairement le projet, les compétences recherchées, la rémunération...\n➡️ Voir la règle 2 de <#218748267431854081>`
      )
      break
    case "salut":
      await interaction.reply(
        `Bonjour, évitez si possible les messages simples tels que "Salut", "Comment ça va" ou "Vous parlez de quoi". Nous sommes beaucoup sur le serveur et si tout le monde le faisait, la discussion serait un peu laborieuse. Lancez plutôt un sujet directement !\n➡️ Voir la règle 3 de <#218748267431854081>`
      )
      break
    case "moteur":
      await interaction.reply(
        `Vous n'arrivez pas à choisir un moteur pour votre projet ?\nNous avons réalisé une vidéo qui résume tout les critères importants, et dans laquelle on liste les meilleurs moteurs du moment !\n➡️ https://youtu.be/VfAM3z45tQU`
      )
      break
    case "debuter":
      await interaction.reply(
        `Créer des jeux vidéos vous semble trop compliqué ?\nVous ne savez pas par où commencer ? Nous avons réalisé une vidéo qui rassemble tous nos conseils et les erreurs à éviter en tant que débutant.\n➡️ https://youtu.be/LgAQWasSAXQ`
      )
      break
  }
})

//////////////////
// Mastodon
//////////////////
const mastodon_posts_stored = new Set()
const mastodon_channel_id = `1040299192226156585`

/**
 * Every hour : fetch our API and clean our stored post
 */
const update_mastodon_channel = () => {
  clean_mastodon_posts()
  fetch_mastodon("trends/links")
  fetch_mastodon("trends/statuses")
}

/**
 * Helper to fetch our Mastodon API and publish on Discord our last trends !
 * @param {*} endpoint
 */
const fetch_mastodon = (endpoint) => {
  fetch(`https://mastodon.gamedevalliance.fr/api/v1/${endpoint}`)
    .then((response) => response.json())
    .then((data) => {
      console.log(`🪶 ${endpoint} successfully fetched ${data.length} posts`)
      pipe(
        compare_mastodon_posts,
        publish_mastodon_posts,
        store_mastodon_posts
      )(data)
    })
    .catch((error) => {
      console.error("🪹 Error while fetching #{endpoint}:", error)
    })
}

/**
 * Compare recentrly fetch posts to our already stored posts, so a same post don't
 * appear in our Discord channel at every fetch
 * @param {Array<Post>} posts_to_compare
 * @returns {Array<Post>} posts not already stored in mastodon_posts_stored
 */
const compare_mastodon_posts = (posts_to_compare) => {
  // Javascript is pure dog💩 , why can't I just set.has() for an object ?
  // And why can't I set.some() or set.values().some() ffs ???
  // And why tf [...set] AND set.values() AND Array.fromSet(set) exists ???
  new_posts = posts_to_compare.filter(
    (post) =>
      ![...mastodon_posts_stored].some(
        (stored_post) =>
          stored_post.includes(post.id) || stored_post.includes(post.blurhash)
      )
  )
  console.log(`🪶 ${new_posts.length} new posts`)
  return new_posts
}

/**
 * We can publish all this trendy trends on our Discord channel
 * @param {Array<Post>} posts_to_publish
 * @returns {Array<Post>}
 */
const publish_mastodon_posts = (posts_to_publish) => {
  // some emoji we want to use
  let wink = client.emojis.cache.get("746349743818407957")
  let happy = client.emojis.cache.get("746352271989669898")
  // actual loop for publishing each post
  posts_to_publish.map((post) => {
    if ("id" in post) {
      send_message_on_channel(
        mastodon_channel_id,
        `${happy} **Nouveau post en tendance :**\n${post.url}`
      )
    } else if ("blurhash" in post) {
      send_message_on_channel(
        mastodon_channel_id,
        `${wink} **Nouvel article en tendance :**\n${post.url}`
      )
    } else throw "type de post inconnu."
  })
  return posts_to_publish
}

/**
 * Store every new posts into mastodon_posts_stored
 * @param {Array<Post>} posts_to_store
 */
const store_mastodon_posts = (posts_to_store) => {
  posts_to_store.map((post) => {
    mastodon_posts_stored.add(
      JSON.stringify({ ...post, stored_at: Date.now() })
    )
  })
}

/**
 * To allow a long-term trending post to reappear on our Discord and for performance
 * confideration, we deleted old stored mastodon posts
 */
const clean_mastodon_posts = () => {
  console.log(`🪶 ${mastodon_posts_stored.size} posts stored before cleaning`)
  mastodon_posts_stored.forEach((post) => {
    if (is_too_old(JSON.parse(post).stored_at))
      mastodon_posts_stored.delete(post)
  })
  console.log(`🪶 ${mastodon_posts_stored.size} posts stored after cleaning`)
}

/**
 * Too old is currently 3 days old, but can be easly changed
 * @param {Date} stored_at
 * @returns {Boolean}
 */
const is_too_old = (stored_at) => {
  return Math.floor((Date.now() - stored_at) / (1000 * 60 * 60 * 24)) >= 3
    ? true
    : false
}

/**
 * Because JS don't have a fk pipe operator
 */
pipe =
  (...fns) =>
  (x) =>
    fns.reduce((v, f) => f(v), x)

// Login to Discord with your client's token
client.login(token)
