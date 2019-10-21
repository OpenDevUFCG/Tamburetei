import PropTypes from 'prop-types'
import React from 'react'
import { useStaticQuery, graphql } from 'gatsby'

const OpenDevLogo = ({ className = '', size = 26 }) => {
  const data = useStaticQuery(graphql`
    query {
      placeholderImage: file(relativePath: { eq: "opendevufcg.svg" }) {
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

OpenDevLogo.propTypes = {
  size: PropTypes.number,
  className: PropTypes.string,
}

export default OpenDevLogo
