import PropTypes from 'prop-types'
import React from 'react'
import { useStaticQuery, graphql } from 'gatsby'

const Logo = ({ className = '', size = 26 }) => {
  const data = useStaticQuery(graphql`
    query {
      placeholderImage: file(relativePath: { eq: "icon.svg" }) {
        publicURL
      }
      site {
        siteMetadata {
          title
        }
      }
    }
  `)

  return (
    <img
      className={className}
      alt={data.site.siteMetadata.title}
      src={data.placeholderImage.publicURL}
      width={size}
      height={size}
    />
  )
}

Logo.propTypes = {
  size: PropTypes.number,
  className: PropTypes.string,
}

export default Logo
