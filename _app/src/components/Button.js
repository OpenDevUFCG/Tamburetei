import classNames from 'classnames'
import PropTypes from 'prop-types'
import React from 'react'

import styles from './Button.module.css'

const Button = ({
  as: Component = 'button',
  size = 'regular',
  className = '',
  ...props
}) => {
  const classes = classNames(className, styles.button, {
    [styles.buttonLarge]: size === 'large',
  })

  return (
    <Component {...props} className={classes}>
      {props.children}
    </Component>
  )
}

Button.propTypes = {
  className: PropTypes.string,
  children: PropTypes.element,
  size: PropTypes.oneOf(['large', 'regular']),
  as: PropTypes.any,
}

export default Button
