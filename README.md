# Textadventure
This is a textadventure maker i did in python!
## how to use
in the adventure.json file, you can make your textadventure. The start command is automaticcaly used at the program startup. To prevent KeyErrors from happening, assign all of your variables there. A command has requirements and replies. Requirements are keywords and variables. They keyword is the command that was typed in. Your command will always need a keyword so it can react to messages. You can make commands acessible in only a certain room. You can have two of the same keywords if they have different requirements, like a different room you have to be in to use the command. Replies are what happens when you use the command. "reply" is the special one here, since this will give a reply. The other ones are all variable changes. For example:
```json
"pick up dagger from chest": {
  "requirements": {
    "keyword": "pick up dagger",
    "room": "lost hut"
  },
  "replies": {
     "reply": "You picked up the dagger.",
     "dagger_in_inventory": true
  }
}
