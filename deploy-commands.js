const { SlashCommandBuilder } = require("@discordjs/builders")
const { REST } = require("@discordjs/rest")
const { Routes } = require("discord-api-types/v9")
const { clientId, guildId, token } = require("./config.json")
/**
 * register slash commands
 */
const commands = [
  new SlashCommandBuilder()
    .setName("question")
    .setDescription("Rappel des règles : poser correctement une question."),
  new SlashCommandBuilder()
    .setName("recrutement")
    .setDescription("Rappel des règles : comment recruter sur Discord ?"),
  new SlashCommandBuilder()
    .setName("salut")
    .setDescription("Rappel des règles : éviter le small talk."),
  new SlashCommandBuilder()
    .setName("help")
    .setDescription("Obtenir la liste des commandes d'Astride par MP."),
  new SlashCommandBuilder()
    .setName("moteur")
    .setDescription("Quel moteur de jeux vidéo utiliser pour un projet ?"),
  new SlashCommandBuilder()
    .setName("debuter")
    .setDescription("Par où commencer dans la création de jeux vidéo ?"),
].map((command) => command.toJSON())

const rest = new REST({ version: "9" }).setToken(token)

rest
  .put(Routes.applicationGuildCommands(clientId, guildId), { body: commands })
  .then(() => console.log("Les commandes ont été remplumées 🪶"))
  .catch(console.error)
