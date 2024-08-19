# Interstellar V6
Interstellar V6 is the latest version of Interstellar
# Deployment
Looking for deployment steps?
https://github.com/UseInterstellar/Interstellar-Astro
# Adding a new app/game:
Make sure to conform to this typescript type below:
```ts
export type Asset = {
  name: string;
  image: string;
  link?: string;
  // or
  links?: { name: string; url: string }[];
  // these fields are optional
  say?: string;
  custom?: boolean;
  partial?: boolean | string;
  error?: boolean | string;
  blank?: boolean | string;
};
```
You do NOT need to convert images to webp. 
