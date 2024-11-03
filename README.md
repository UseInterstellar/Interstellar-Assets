# Interstellar Assets

Welcome to the Interstellar Assets repository! This repository is dedicated to adding and managing games and applications for our site.

## Looking for Deployment Steps?

You can find comprehensive deployment instructions [here](https://github.com/UseInterstellar/Interstellar-Astro).

## Adding Apps/Games

To successfully add an app or game to the repository, please follow these steps:

1. Navigate to the `/json` directory and locate the appropriate file for your addition.
2. Include a link to the website and an image that represents the app/game. If an icon does not exist, you may leave the image field blank.

### Asset Structure

Ensure your additions adhere to the following TypeScript type:

```ts
export type Asset = {
  // Required fields
  name: string;          // (Required) The name of the app/game
  image: string;         // (Required) The path to the image/icon
  link: string;          // (Required) The URL link to the website

  // Optional fields
  say?: string;             // (Optional) Additional information or notes
  error?: boolean | string; // (Optional) Indicator for errors
  blank?: boolean | string; // (Optional) Indicates if a game only works outside of an iframe
};
```

## Final Steps

After making your changes, run the following commands to rename the icons and minify the JSON files:

```bash
python rename.py && python minify.py
```
