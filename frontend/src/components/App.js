import React, { useState, useCallback, Component } from "react";
import { render } from "react-dom";
import Gallery from "react-photo-gallery";
import Carousel, { Modal, ModalGateway } from "react-images";

function Photos(props) {
  const [state, setState] = useState([])

  const [currentImage, setCurrentImage] = useState(0);
  const [viewerIsOpen, setViewerIsOpen] = useState(false);

  const openLightbox = useCallback((event, { photo, index }) => {
    setCurrentImage(index);
    setViewerIsOpen(true);
  }, []);

  const closeLightbox = () => {
    setCurrentImage(0);
    setViewerIsOpen(false);
  };

  return (
    <div>
      <div className="row justify-content-center mb-2 pb-3">
        <div className="col-md-7 heading-section heading-section-2 text-center ftco-animate fadeInUp ftco-animated">
          <h2 className="mb-4">Ostatnio dodane zdjęcia</h2>
          <h5 className="mb-4">Kliknij na zdjęcie, aby powiększyć</h5>
        </div>
      </div>
      <Gallery photos={props.photos} onClick={openLightbox} />
      <ModalGateway>
        {viewerIsOpen ? (
          <Modal onClose={closeLightbox}>
            <Carousel
              currentIndex={currentImage}
              views={props.photos.map(x => ({
                src: x.image,
                srcset: x.srcSet,
                caption: x.title,
              }))}
            />
          </Modal>
        ) : null}
      </ModalGateway>
    </div>
  );
}


class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      count: 0,
    };
  }

  componentDidMount() {
    this.getData()
  }

  componentDidUpdate(prevProps, prevState, snapshot) {
    if (this.state.count !== prevState.count) {
      window.scrollTo(0,document.getElementById('first').clientHeight)
      this.getData()
    }

  }

  increment() {
    this.setState({
      count: this.state.count + 10,
    });
  };

  getData() {
    fetch("api/top/?format=json&limit=10&offset=" + this.state.count + "")
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(data => {
        this.setState({ data: data.results, next: data.next })
      });
  }

  render() {
    const dataLoaded = this.state.data.length;
    const next = this.state.next;
    return (
      <>
        {dataLoaded ? <Photos photos={this.state.data} /> :
          <h3>Ładowanie galerii zdjęć...</h3>
         }
        {next ? <button className='btn-show-more' onClick={(e) => this.increment(e)}>Pokaż więcej</button>:""}
      </>
    );
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);
