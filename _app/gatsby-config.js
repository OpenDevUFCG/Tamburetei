module.exports = {
  siteMetadata: {
    title: 'Tamburetei',
    description: 'Fazendo de tamburete as cadeiras de CC@UFCG',
    author: '@OpenDevUFCG',
  },
  plugins: [
    'gatsby-plugin-react-helmet',
    {
      resolve: 'gatsby-source-filesystem',
      options: {
        path: `${__dirname}/..`,
        name: 'subjects',
        ignore: ['**/\\.*', '**/\\.*/**/*', '**/_app/**/*', '**/scripts/**/*'],
      },
    },
    {
      resolve: 'gatsby-source-filesystem',
      options: {
        path: `${__dirname}/content/assets`,
        name: 'assets',
      },
    },
    {
      resolve: 'gatsby-transformer-remark',
      options: {
        plugins: ['gatsby-remark-autolink-headers', 'gatsby-remark-tamburetei'],
      },
    },
    'gatsby-transformer-sharp',
    'gatsby-plugin-sharp',
    {
      resolve: 'gatsby-plugin-manifest',
      options: {
        name: 'Tamburetei',
        short_name: 'Tamburetei',
        start_url: '/',
        background_color: '#ffffff',
        theme_color: '#ffffff',
        display: 'standalone',
        icon: 'content/assets/icon.svg',
      },
    },
    {
      resolve: 'gatsby-plugin-google-fonts',
      options: {
        fonts: ['Roboto'],
      },
    },
    'gatsby-plugin-sass',
  ],
}
